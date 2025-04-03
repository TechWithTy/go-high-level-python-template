from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_note(
    token: str,
    contact_id: str,
    body: str,
    user_id: str = None
) -> Dict[str, Any]:
    """
    Create a note for a contact in Go High Level.
    
    Args:
        token: Authentication token
        contact_id: The ID of the contact to add the note to
        body: The content of the note
        user_id: Optional user ID associated with the note
        
    Returns:
        Dictionary containing the created note data
        
    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/contacts/{contact_id}/notes"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {"body": body}
    if user_id:
        payload["userId"] = user_id
    
    logging.info(f"Creating note for contact: {contact_id}")
    
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                url,
                headers=headers,
                json=payload
            )
            
        if response.status_code != 201:
            error_detail = response.text
            logging.error(f"API request failed with status {response.status_code}: {error_detail}")
            raise Exception(f"Failed to create note: {error_detail}")
            
        return response.json()
        
    except Exception as e:
        logging.error(f"Error creating note: {str(e)}")
        raise