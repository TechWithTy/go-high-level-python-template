import requests
import json

def create_contact(auth_token, version="2021-07-28", **contact_data):
    """
    Create a contact in Go High Level
    
    Args:
        auth_token (str): Authorization token
        version (str): API version, defaults to "2021-07-28"
        **contact_data: Contact data fields (firstName, lastName, etc.)
    
    Returns:
        dict: API response
    """
    url = "https://services.leadconnectorhq.com/contacts/"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "Version": version
    }
    
    response = requests.post(url, headers=headers, json=contact_data)
    return response.json()  