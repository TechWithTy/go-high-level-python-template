from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def fetch_timezones(location_id: str, access_token: str) -> Dict[str, Any]:
    """
    Fetch available timezones for a location in Go High Level.

    Args:
        location_id: The ID of the location
        access_token: The access token for authentication

    Returns:
        Dictionary containing the timezones data

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/locations/{location_id}/timezones"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()