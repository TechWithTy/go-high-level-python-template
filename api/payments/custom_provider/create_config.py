from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_custom_provider_config(
    access_token: str,
    location_id: str,
    live_api_key: str,
    live_publishable_key: str,
    test_api_key: str,
    test_publishable_key: str
) -> Dict[str, Any]:
    """
    Create a new custom provider payment config for a given location.

    Args:
        access_token (str): The access token for authentication.
        location_id (str): The location ID.
        live_api_key (str): API key for live payments.
        live_publishable_key (str): Publishable key for live payments.
        test_api_key (str): API key for test payments.
        test_publishable_key (str): Publishable key for test payments.

    Returns:
        Dict[str, Any]: The response data from the API.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/payments/custom-provider/connect"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    params = {
        "locationId": location_id
    }

    data = {
        "live": {
            "apiKey": live_api_key,
            "publishableKey": live_publishable_key
        },
        "test": {
            "apiKey": test_api_key,
            "publishableKey": test_publishable_key
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()