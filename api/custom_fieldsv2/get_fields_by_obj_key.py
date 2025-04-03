from typing import Dict, Any, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_fields_by_obj_key(
    token: str,
    object_key: str,
    location_id: str
) -> Dict[str, Any]:
    """
    Get Custom Fields By Object Key.
    
    Only supports Custom Objects and Company (Business) today.
    
    Args:
        token: The authorization token
        object_key: Key of the Object (must include "custom_objects." prefix for custom objects)
        location_id: Location ID
        
    Returns:
        Dictionary containing custom fields data for the object
        
    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/custom-fields/object-key/{object_key}"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }
    
    params = {
        "locationId": location_id
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            logging.error(f"Failed to get custom fields: {response.text}")
            response.raise_for_status()
            
        return response.json()