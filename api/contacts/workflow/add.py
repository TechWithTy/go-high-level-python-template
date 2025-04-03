from typing import Dict, Any, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def add_contact_to_workflow(
    contact_id: str,
    workflow_id: str,
    auth_token: str,
    event_start_time: Optional[str] = None
) -> Dict[str, Any]:
    """
    Add a contact to a workflow in Go High Level.
    
    Args:
        contact_id: ID of the contact
        workflow_id: ID of the workflow
        auth_token: Bearer token for authentication
        event_start_time: Optional start time for the workflow event in ISO format (e.g. "2021-06-23T03:30:00+01:00")
        
    Returns:
        Dict containing the API response
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {}
    if event_start_time:
        payload["eventStartTime"] = event_start_time
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{API_BASE_URL}/contacts/{contact_id}/workflow/{workflow_id}",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logging.error(f"Error adding contact {contact_id} to workflow {workflow_id}: {str(e)}")
        raise