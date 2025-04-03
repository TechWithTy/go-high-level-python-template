from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_custom_values(location_id: str, access_token: str) -> Dict[str, Any]:
    """
    Get Custom Values for a location in Go High Level.

    Args:
        location_id: The ID of the location
        access_token: The access token for authentication

    Returns:
        Dictionary containing the custom values data

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/locations/{location_id}/customValues"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise Exception(f"Failed to get custom values: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred while getting custom values: {e}")