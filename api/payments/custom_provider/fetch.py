from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def fetch_custom_provider(access_token: str, location_id: str) -> Dict[str, Any]:
    """
    Fetch an existing payment config for a given location.

    Args:
        access_token (str): The access token for authentication.
        location_id (str): The ID of the location.

    Returns:
        Dict[str, Any]: The custom provider configuration.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/payments/custom-provider/connect"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }
    
    params = {
        "locationId": location_id
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()