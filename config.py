import os
from dotenv import load_dotenv
load_dotenv()

ENV = os.getenv("ENV", "dev")
TIKTOK_CLIENT_ID = os.getenv("TIKTOK_CLIENT_ID", "mock_client_id")
TIKTOK_CLIENT_SECRET = os.getenv("TIKTOK_CLIENT_SECRET", "mock_client_secret")

TIKTOK_REDIRECT_URI = os.getenv(
    "TIKTOK_REDIRECT_URI",
    "http://localhost:8000/oauth/callback"
)

TIKTOK_SCOPES = [
    "ads.manage",
    "ads.read"
]

TIKTOK_AUTH_URL = "https://ads.tiktok.com/marketing_api/auth"
TIKTOK_TOKEN_URL = "https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/"

TIKTOK_API_BASE = "https://business-api.tiktok.com/open_api/v1.3"

USE_MOCK_API = True
