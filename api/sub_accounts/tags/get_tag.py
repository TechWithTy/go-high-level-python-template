from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_tag(location_id: str, tag_id: str, access_token: str) -> Dict[str, Any]:
    """
    Get tag by id from Go High Level API.

    Args:
        location_id: The ID of the location
        tag_id: The ID of the tag
        access_token: The access token for authentication

    Returns:
        Dictionary containing the tag data

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/locations/{location_id}/tags/{tag_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()