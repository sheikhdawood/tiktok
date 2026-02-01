import requests
from config import (
    TIKTOK_CLIENT_ID,
    TIKTOK_CLIENT_SECRET,
    TIKTOK_REDIRECT_URI,
    TIKTOK_SCOPES,
    TIKTOK_AUTH_URL,
    TIKTOK_TOKEN_URL
)

class OAuthError(Exception):
    def __init__(self, message, suggestion=None):
        self.message = message
        self.suggestion = suggestion
        super().__init__(message)

def get_authorization_url(state: str) -> str:
    scope = ",".join(TIKTOK_SCOPES)

    return (
        f"{TIKTOK_AUTH_URL}"
        f"?app_id={TIKTOK_CLIENT_ID}"
        f"&redirect_uri={TIKTOK_REDIRECT_URI}"
        f"&state={state}"
        f"&scope={scope}"
        f"&response_type=code"
    )

def exchange_code_for_token(code: str) -> dict:
    payload = {
        "app_id": TIKTOK_CLIENT_ID,
        "secret": TIKTOK_CLIENT_SECRET,
        "auth_code": code
    }

    response = requests.post(TIKTOK_TOKEN_URL, json=payload)

    if response.status_code != 200:
        raise OAuthError(
            "Failed to contact TikTok OAuth server.",
            "Check network connectivity."
        )

    data = response.json()

    if "access_token" not in data:
        error_code = data.get("code")

        if error_code == 401:
            raise OAuthError(
                "Invalid client ID or client secret.",
                "Verify your TikTok app credentials."
            )

        if error_code == 403:
            raise OAuthError(
                "Missing required Ads permissions.",
                "Ensure ads.manage scope is enabled."
            )

        raise OAuthError(
            "OAuth authorization failed.",
            "Re-authenticate the application."
        )

    return {
        "access_token": data["access_token"],
        "expires_in": data.get("expires_in"),
        "refresh_token": data.get("refresh_token")
    }
