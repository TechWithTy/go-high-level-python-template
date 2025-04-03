from typing import Dict, Any, List, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_contacts_by_business_id(
    business_id: str,
    location_id: str,
    auth_token: str,
    limit: int = 25,
    query: Optional[str] = None,
    skip: int = 0
) -> Dict[str, Any]:
    """
    Get contacts by business ID.
    
    Args:
        business_id: The ID of the business
        location_id: The ID of the location
        auth_token: Authorization token
        limit: Maximum number of results to return (default: 25)
        query: Optional search query for contact name
        skip: Number of results to skip (default: 0)
        
    Returns:
        Dict containing contacts and count
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }
    
    params = {
        "locationId": location_id,
        "limit": limit,
        "skip": skip
    }
    
    if query:
        params["query"] = query
    
    url = f"{API_BASE_URL}/contacts/business/{business_id}"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"Error fetching contacts by business ID: {e}")
        raise