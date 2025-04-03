from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_csv_post(
    access_token: str,
    location_id: str,
    csv_id: str,
    post_id: str
) -> Dict[str, Any]:
    """
    Delete a CSV post.

    Args:
        access_token: Access token for authentication
        location_id: The ID of the location
        csv_id: The ID of the CSV
        post_id: The ID of the post to delete

    Returns:
        Dictionary containing the API response

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/csv/{csv_id}/post/{post_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()