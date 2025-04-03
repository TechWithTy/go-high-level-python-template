from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_custom_field_by_id(field_id: str, token: str) -> Dict[Any, Any]:
    """
    Get Custom Field / Folder By Id.
    Only supports Custom Objects and Company (Business) today.
    
    Args:
        field_id: The ID of the custom field to retrieve
        token: The authorization token
        
    Returns:
        Dict containing the custom field data
    """
    url = f"{API_BASE_URL}/custom-fields/{field_id}"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise