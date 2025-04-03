from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def start_csv_finalize(
    access_token: str,
    location_id: str,
    csv_id: str,
    user_id: str
) -> Dict[str, Any]:
    """
    Start CSV finalization process.

    Args:
        access_token: The access token for authentication
        location_id: The ID of the location
        csv_id: The ID of the CSV
        user_id: The ID of the user

    Returns:
        Dictionary containing the API response

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/csv/{csv_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = {"userId": user_id}

    async with httpx.AsyncClient() as client:
        response = await client.patch(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()