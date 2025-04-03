from typing import Dict, Any, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_custom_fields(
    token: str,
    location_id: str,
    model: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get Custom Fields for a location in Go High Level.

    Args:
        token: Access Token
        location_id: Location Id
        model: Model of the custom field to retrieve (optional)

    Returns:
        Dictionary containing the custom fields data

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/locations/{location_id}/customFields"

    headers = {
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {}
    if model:
        params["model"] = model

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise