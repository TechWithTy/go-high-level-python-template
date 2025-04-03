from typing import Dict, Any, List
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def add_tags_to_contact(
    contact_id: str,
    tags: List[str],
    auth_token: str
) -> Dict[str, Any]:
    """
    Add tags to a contact in Go High Level.
    
    Args:
        contact_id: The ID of the contact to add tags to
        tags: List of tag strings to add to the contact
        auth_token: Bearer token for authentication
        
    Returns:
        Dictionary containing the added tags
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "tags": tags
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{API_BASE_URL}/contacts/{contact_id}/tags",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logging.error(f"Error adding tags to contact {contact_id}: {str(e)}")
        raise