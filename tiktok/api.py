from tiktok.errors import TikTokAPIError
import random

def submit_ad(payload: dict) -> dict:
    failure = None

    if failure:
        raise TikTokAPIError(failure)

    return {
        "status": "success",
        "campaign_id": "cmp_12345"
    }
