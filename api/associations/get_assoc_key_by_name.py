from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_association_key_by_name(
    token: str,
    key_name: str,
    location_id: str
) -> Dict[str, Any]:
    """
    Get association key by name from Go High Level API.
    
    Args:
        token: The authorization token
        key_name: The name of the association key
        location_id: The location ID
        
    Returns:
        Dictionary containing the association key data
    """
    url = f"{API_BASE_URL}/associations/key/{key_name}"
    
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
            logging.error(f"Failed to get association key by name: {response.text}")
            response.raise_for_status()
            
        return response.json()