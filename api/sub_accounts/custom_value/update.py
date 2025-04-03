from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_custom_value(
    location_id: str,
    custom_value_id: str,
    headers: Dict[str, str],
    name: str,
    value: str
) -> Dict[str, Any]:
    """
    Update a custom value in Go High Level.

    Args:
        location_id: The ID of the location
        custom_value_id: The ID of the custom value to update
        headers: Dictionary containing Authorization and Version headers
        name: The name of the custom field
        value: The value to set for the custom field

    Returns:
        Dictionary containing the updated custom value data

    Raises:
        Exception: If the API request fails or if required headers are missing
    """
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise Exception("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    if not headers.get("Version"):
        headers["Version"] = API_VERSION

    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers["Version"],
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
            response = await client.put(url, headers=request_headers, json=data)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise Exception(f"Failed to update custom value: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred while updating custom value: {e}")