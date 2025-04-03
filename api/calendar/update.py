import requests
import json

def update_calendar(calendar_id, access_token, data):
    """
    Update a calendar by ID in Go High Level.
    
    Args:
        calendar_id (str): The ID of the calendar to update
        access_token (str): The access token for authentication
        data (dict): The calendar data to update
        
    Returns:
        dict: The response from the API
    """
    url = f"https://services.leadconnectorhq.com/calendars/{calendar_id}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": "2021-04-15",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    response = requests.put(url, headers=headers, json=data)
    return response.json()  