from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_custom_value(
    location_id: str,
    custom_value_id: str,
    access_token: str,
    name: str,
    value: str
) -> Dict[str, Any]:
    """
    Update a custom value in Go High Level.

    Args:
        location_id: The ID of the location
        custom_value_id: The ID of the custom value to update
        access_token: The access token for authentication
        name: The name of the custom field
        value: The value to set for the custom field

    Returns:
        Dictionary containing the updated custom value data

    Raises:
        Exception: If the API request fails
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    url = f"{API_BASE_URL}/locations/{location_id}/customValues/{custom_value_id}"

    data = {
        "name": name,
        "value": value
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise Exception(f"Failed to update custom value: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred while updating custom value: {e}")