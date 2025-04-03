from typing import Dict, Any, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_authors(
    location_id: str,
    access_token: str,
    limit: int = 5,
    offset: int = 0
) -> Dict[str, Any]:
    """
    Get all authors for a given location ID.

    Args:
        location_id: The ID of the location
        access_token: The access token for authentication
        limit: Number of authors to show in the listing (default: 5)
        offset: Number of authors to skip in listing (default: 0)

    Returns:
        Dictionary containing the authors data

    Raises:
        Exception: If the API request fails
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "locationId": location_id,
        "limit": limit,
        "offset": offset
    }

    url = f"{API_BASE_URL}/blogs/authors"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"Error fetching authors: {e}")
        raise