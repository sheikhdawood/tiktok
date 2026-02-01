class TikTokAPIError(Exception):
    def __init__(self, code):
        self.code = code
        super().__init__(code)

def explain_api_error(error: Exception) -> str:
    if error.code == "INVALID_TOKEN":
        return (
            "❌ Your TikTok access token is invalid or expired.\n"
            "➡️ Please re-authenticate to continue."
        )

    if error.code == "INVALID_MUSIC":
        return (
            "❌ The selected music is not approved for ads.\n"
            "➡️ Choose a different music ID or upload custom music."
        )

    if error.code == "GEO_BLOCK":
        return (
            "❌ TikTok Ads are not available in your current region.\n"
            "➡️ Verify your ad account location."
        )

    return "❌ An unknown error occurred."
