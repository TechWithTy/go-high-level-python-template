from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_google_business_locations(
    access_token: str,
    location_id: str,
    account_id: str
) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    url = f"{API_BASE_URL}/social-media-posting/oauth/{location_id}/google/locations/{account_id}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()