from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_opportunity(opportunity_id: str, access_token: str) -> Dict[str, Any]:
    """
    Get an opportunity by its ID.

    Args:
        opportunity_id (str): The ID of the opportunity to retrieve.
        access_token (str): The access token for authentication.

    Returns:
        Dict[str, Any]: The opportunity data.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/opportunities/{opportunity_id}"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()