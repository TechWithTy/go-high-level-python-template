from typing import Dict, Any, List
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_all_tasks(contact_id: str, auth_token: str) -> Dict[str, Any]:
    """
    Get all tasks for a specific contact from the Go High Level API.
    
    Args:
        contact_id: The ID of the contact to get tasks for
        auth_token: The authorization token for the API
        
    Returns:
        Dict containing the tasks data
    """
    url = f"{API_BASE_URL}/contacts/{contact_id}/tasks"
    
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise