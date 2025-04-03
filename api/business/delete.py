import os
import requests
from typing import Dict, Any

API_BASE_URL = "https://services.leadconnectorhq.com"

def delete_business(business_id: str, auth_token: str, version: str = "2021-07-28") -> Dict[str, bool]:
    """
    Delete a business by ID using the Go High Level API.
    
    :param business_id: The ID of the business to delete.
    :param auth_token: Access Token for authentication.
    :param version: API version, defaults to "2021-07-28".
    :return: JSON response data from the API.
    """
    url = f"{API_BASE_URL}/businesses/{business_id}"
    
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Version": version,
        "Accept": "application/json"
    }
    
    response = requests.delete(url, headers=headers)
    
    if not response.ok:
        error_text = response.text
        raise Exception(f"Error deleting business: {error_text}")
        
    return response.json()  # Returns {"success": true}