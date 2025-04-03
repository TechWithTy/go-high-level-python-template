from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def add_contact_to_campaign(
    contact_id: str,
    campaign_id: str,
    auth_token: str
) -> Dict[str, Any]:
    """
    Add a contact to a campaign in Go High Level.
    
    Args:
        contact_id: The ID of the contact to add to the campaign
        campaign_id: The ID of the campaign to add the contact to
        auth_token: Bearer token for authentication
        
    Returns:
        Dictionary containing the response data
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{API_BASE_URL}/contacts/{contact_id}/campaigns/{campaign_id}",
                json={},
                headers=headers
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logging.error(f"Error adding contact {contact_id} to campaign {campaign_id}: {str(e)}")
        raise