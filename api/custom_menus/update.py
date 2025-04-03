from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_custom_menu(access_token: str, custom_menu_id: str) -> Dict[str, Any]:
    """
    Delete a custom menu.

    Args:
        access_token (str): The access token for authentication.
        custom_menu_id (str): The ID of the custom menu to delete.

    Returns:
        Dict[str, Any]: A dictionary containing the API response.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/custom-menus/{custom_menu_id}"

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