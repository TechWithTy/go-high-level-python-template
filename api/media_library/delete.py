from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_media(
    access_token: str,
    media_id: str,
    alt_id: str,
    alt_type: str
) -> Dict[str, Any]:
    """
    Delete a specific file or folder from the media library.

    Args:
        access_token: The access token for authentication
        media_id: The ID of the media to delete
        alt_id: Location or agency ID
        alt_type: AltType (must be 'location' or 'agency')

    Returns:
        Dictionary containing the deletion response

    Raises:
        Exception: If the API request fails
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "altId": alt_id,
        "altType": alt_type
    }

    logging.info(f"Deleting media with ID: {media_id}")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{API_BASE_URL}/medias/{media_id}",
                headers=headers,
                params=params
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise Exception(f"Failed to delete media: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred while deleting media: {e}")