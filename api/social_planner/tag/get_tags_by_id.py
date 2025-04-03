from typing import Dict, Any, List
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_tags_by_ids(access_token: str, location_id: str, tag_ids: List[str]) -> Dict[str, Any]:
    """
    Get tags by ids.

    Args:
        access_token: The access token for authentication.
        location_id: The ID of the location.
        tag_ids: List of tag IDs to fetch.

    Returns:
        A dictionary containing the API response.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/tags/details"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }

    data = {"tagIds": tag_ids}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()