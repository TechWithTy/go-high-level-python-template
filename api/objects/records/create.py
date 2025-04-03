from typing import Dict, Any, List, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_record(
    schema_key: str,
    record_data: Dict[str, Any],
    headers: Dict[str, str]
) -> Dict[str, Any]:
    """
    Create a Custom Object Record in Go High Level.
    
    Args:
        schema_key: The key of the Custom Object / Standard Object Schema.
                   For custom objects, include the "custom_objects." prefix.
                   For standard objects, use their respective object keys.
        record_data: Dictionary containing record properties, owner, followers, etc.
        headers: Dictionary containing Authorization and Version headers
        
    Returns:
        Dictionary containing the created record data
        
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
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    logging.info(f"Creating record for schema: {schema_key}")
    
    try:
        # Make the API request to create record
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                f"{API_BASE_URL}/objects/{schema_key}/records",
                headers=request_headers,
                json=record_data
            )
            
        # Handle the API response
        if response.status_code != 201:
            error_detail = response.text
            logging.error(f"API request failed with status {response.status_code}: {error_detail}")
            raise Exception(f"API request failed with status {response.status_code}: {error_detail}")
        
        return response.json()
        
    except Exception as e:
        logging.error(f"Error creating record: {str(e)}")
        raise