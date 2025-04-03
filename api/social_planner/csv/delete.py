from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_csv(access_token: str, location_id: str, csv_id: str) -> Dict[str, Any]:
    """
    Delete a CSV file.

    Args:
        access_token: The access token for authentication
        location_id: The ID of the location
        csv_id: The ID of the CSV to delete

    Returns:
        Dictionary containing the API response

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/csv/{csv_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()