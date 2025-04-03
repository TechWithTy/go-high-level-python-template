from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def disconnect_custom_provider(access_token: str, location_id: str, live_mode: bool) -> Dict[str, Any]:
    """
    Disconnect an existing payment config for a given location.

    Args:
        access_token (str): The access token for authentication.
        location_id (str): The ID of the location.
        live_mode (bool): Whether the config is for test mode or live mode.

    Returns:
        Dict[str, Any]: The response data from the API.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/payments/custom-provider/disconnect"

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
        "liveMode": live_mode
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()