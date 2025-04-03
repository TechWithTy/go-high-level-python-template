from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_tag(
    location_id: str,
    tag_id: str,
    access_token: str,
    name: str
) -> Dict[str, Any]:
    """
    Update a tag in Go High Level.

    Args:
        location_id: The ID of the location
        tag_id: The ID of the tag to update
        access_token: The access token for authentication
        name: The new name for the tag

    Returns:
        Dictionary containing the updated tag data

    Raises:
        Exception: If the API request fails
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    url = f"{API_BASE_URL}/locations/{location_id}/tags/{tag_id}"

    data = {
        "name": name
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise Exception(f"Failed to update tag: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred while updating tag: {e}")