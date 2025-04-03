from typing import Dict, Any, List
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_links(access_token: str, location_id: str) -> List[Dict[str, Any]]:
    """
    Get links from the Go High Level API.

    Args:
        access_token: The access token for authentication
        location_id: The ID of the location

    Returns:
        A list of dictionaries containing link data

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/links/"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }
    
    params = {
        "locationId": location_id
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            logging.error(f"Failed to get links: {response.text}")
            response.raise_for_status()
        
        return response.json().get("links", [])