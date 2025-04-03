from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_task_to_complete(
    contact_id: str,
    task_id: str,
    auth_token: str,
    completed: bool = True
) -> Dict[str, Any]:
    """
    Update a task's completed status for a contact in Go High Level.
    
    Args:
        contact_id: ID of the contact
        task_id: ID of the task to update
        auth_token: Bearer token for authentication
        completed: Whether the task is completed (defaults to True)
        
    Returns:
        Dict containing the updated task data
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "completed": completed
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{API_BASE_URL}/contacts/{contact_id}/tasks/{task_id}/completed",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise