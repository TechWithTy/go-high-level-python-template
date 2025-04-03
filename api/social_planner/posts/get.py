from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_post(access_token: str, location_id: str, post_id: str) -> Dict[str, Any]:
    """
    Get a social media post from Go High Level API.

    Args:
        access_token: The access token for authentication
        location_id: The ID of the location
        post_id: The ID of the post to retrieve

    Returns:
        Dictionary containing the post data

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/posts/{post_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()