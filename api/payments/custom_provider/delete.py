from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_custom_provider(access_token: str, location_id: str) -> Dict[str, Any]:
    """
    Delete an existing custom provider integration.

    Args:
        access_token (str): The access token for authentication.
        location_id (str): The location ID.

    Returns:
        Dict[str, Any]: The response data from the API.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/payments/custom-provider/provider"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "locationId": location_id
    }

    async with httpx.AsyncClient() as client:
        response = await client.delete(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()