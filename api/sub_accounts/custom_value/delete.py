from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_custom_value(
    location_id: str,
    custom_value_id: str,
    access_token: str
) -> Dict[str, Any]:
    """
    Delete a custom value for a specific location.

    Args:
        location_id: The ID of the location
        custom_value_id: The ID of the custom value to delete
        access_token: The access token for authentication

    Returns:
        Dict containing the API response

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/locations/{location_id}/customValues/{custom_value_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise