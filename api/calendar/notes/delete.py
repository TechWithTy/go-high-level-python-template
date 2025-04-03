from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-04-15"

async def delete_note(
    appointment_id: str,
    note_id: str,
    headers: Dict[str, str]
) -> Dict[str, bool]:
    """
    Delete a note from an appointment in the Go High Level API.
    
    Args:
        appointment_id: The ID of the appointment
        note_id: The ID of the note to delete
        headers: Dictionary containing Authorization and Version headers
        
    Returns:
        Dictionary containing success status
        
    Raises:
        Exception: If the API request fails or if required headers are missing
    """
    # Validate required headers
    if not headers.get("Authorization") or not headers["Authorization"].startswith("Bearer "):
        raise Exception("Missing or invalid Authorization header. Must be in format: 'Bearer {token}'")

    if not headers.get("Version"):
        # Set default version if not provided
        headers["Version"] = API_VERSION
    
    # Prepare request headers
    request_headers = {
        "Authorization": headers["Authorization"],
        "Version": headers["Version"],
        "Accept": "application/json"
    }
    
    logging.info(f"Making request to delete note {note_id} from appointment: {appointment_id}")
    
    try:
        # Make the API request to delete note
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.delete(
                f"{API_BASE_URL}/calendars/appointments/{appointment_id}/notes/{note_id}",
                headers=request_headers
            )
            
        # Handle the API response
        if response.status_code != 200:
            error_detail = response.text
            logging.error(f"API request failed with status {response.status_code}: {error_detail}")
            raise Exception(f"API request failed with status {response.status_code}: {error_detail}")
            
        return response.json()
        
    except Exception as e:
        logging.error(f"Error deleting note: {str(e)}")
        raise