from typing import Dict, Any, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_duplicate_contact(
    token: str,
    location_id: str,
    email: Optional[str] = None,
    number: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get duplicate contact from Go High Level.
    
    If Allow Duplicate Contact is disabled under Settings, the global unique identifier 
    will be used for searching the contact. If the setting is enabled, first priority 
    for search is email and the second priority will be phone.
    
    Args:
        token: Bearer token for authentication
        location_id: The ID of the location
        email: Contact email (optional)
        number: Contact phone number (optional)
        
    Returns:
        Dictionary containing contact data
    """
    url = f"{API_BASE_URL}/contacts/search/duplicate"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }
    
    params = {
        "locationId": location_id
    }
    
    if email:
        params["email"] = email
    
    if number:
        params["number"] = number
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"Error fetching duplicate contact: {e}")
        raise