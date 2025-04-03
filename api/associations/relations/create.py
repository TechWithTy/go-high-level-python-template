from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_relation(
    token: str,
    location_id: str,
    association_id: str,
    first_record_id: str,
    second_record_id: str
) -> Dict[str, Any]:
    """
    Create a relation between associated entities in Go High Level.
    
    Args:
        token: The authorization token
        location_id: The location ID (Sub Account ID)
        association_id: The ID of the association
        first_record_id: ID of the first record (e.g., contactId)
        second_record_id: ID of the second record (e.g., customObject record ID)
        
    Returns:
        Dictionary containing the created relation data
    """
    url = f"{API_BASE_URL}/associations/relations"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "locationId": location_id,
        "associationId": association_id,
        "firstRecordId": first_record_id,
        "secondRecordId": second_record_id
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        
        if response.status_code != 201:
            logging.error(f"Failed to create relation: {response.text}")
            response.raise_for_status()
            
        return response.json()