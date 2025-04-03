from typing import Dict, Any, List
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def bulk_update_contacts_business(
    location_id: str,
    contact_ids: List[str],
    business_id: str,
    auth_token: str
) -> Dict[str, Any]:
    """
    Add or remove contacts from a business in Go High Level.
    
    Args:
        location_id: The ID of the location
        contact_ids: List of contact IDs to add/remove
        business_id: The ID of the business to add contacts to (or None to remove)
        auth_token: Bearer token for authentication
        
    Returns:
        Dictionary containing success status and processed IDs
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "locationId": location_id,
        "ids": contact_ids,
        "businessId": business_id
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{API_BASE_URL}/contacts/bulk/business",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logging.error(f"Error updating bulk contacts business: {str(e)}")
        raise