from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_custom_field(
    location_id: str,
    custom_field_id: str,
    access_token: str,
    custom_field_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Update a custom field in Go High Level.

    Args:
        location_id: The ID of the location
        custom_field_id: The ID of the custom field to update
        access_token: The access token for authentication
        custom_field_data: Dictionary containing custom field details to update

    Returns:
        Dictionary containing the updated custom field data

    Raises:
        Exception: If the API request fails
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    logging.info(f"Updating custom field {custom_field_id} for location {location_id}")

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.put(
                f"{API_BASE_URL}/locations/{location_id}/customFields/{custom_field_id}",
                headers=headers,
                json=custom_field_data
            )

        if response.status_code != 200:
            error_detail = response.text
            logging.error(f"API request failed with status {response.status_code}: {error_detail}")
            raise Exception(f"API request failed with status {response.status_code}: {error_detail}")

        return response.json()

    except httpx.RequestError as e:
        logging.error(f"An error occurred while making the request: {str(e)}")
        raise Exception(f"An error occurred while making the request: {str(e)}")