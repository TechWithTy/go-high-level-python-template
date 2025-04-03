from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_sub_account(
    location_id: str,
    access_token: str,
    delete_twilio_account: bool = False
) -> Dict[str, Any]:
    """
    Delete a Sub-Account (Formerly Location) from the Agency.

    Args:
        location_id: The ID of the location to delete
        access_token: The access token for authentication
        delete_twilio_account: Boolean to indicate whether to delete Twilio Account or not

    Returns:
        Dict containing the API response

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/locations/{location_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "deleteTwilioAccount": str(delete_twilio_account).lower()
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise