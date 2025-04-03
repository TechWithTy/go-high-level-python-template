from typing import Dict, Any, List, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def upsert_contact(
    token: str,
    location_id: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    name: Optional[str] = None,
    email: Optional[str] = None,
    gender: Optional[str] = None,
    phone: Optional[str] = None,
    address1: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None,
    postal_code: Optional[str] = None,
    website: Optional[str] = None,
    timezone: Optional[str] = None,
    dnd: Optional[bool] = None,
    dnd_settings: Optional[Dict[str, Any]] = None,
    inbound_dnd_settings: Optional[Dict[str, Any]] = None,
    tags: Optional[List[str]] = None,
    custom_fields: Optional[List[Dict[str, str]]] = None,
    source: Optional[str] = None,
    country: Optional[str] = None,
    company_name: Optional[str] = None,
    assigned_to: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Upsert a contact in Go High Level.
    
    If Allow Duplicate Contact is disabled under Settings, the global unique identifier 
    will be used for de-duplication. If the setting is enabled, a new contact will 
    get created with the shared details.
    """
    url = f"{API_BASE_URL}/contacts/upsert"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "locationId": location_id
    }
    
    # Add optional fields to payload
    if first_name:
        payload["firstName"] = first_name
    if last_name:
        payload["lastName"] = last_name
    if name:
        payload["name"] = name
    if email:
        payload["email"] = email
    if gender:
        payload["gender"] = gender
    if phone:
        payload["phone"] = phone
    if address1:
        payload["address1"] = address1
    if city:
        payload["city"] = city
    if state:
        payload["state"] = state
    if postal_code:
        payload["postalCode"] = postal_code
    if website:
        payload["website"] = website
    if timezone:
        payload["timezone"] = timezone
    if dnd is not None:
        payload["dnd"] = dnd
    if dnd_settings:
        payload["dndSettings"] = dnd_settings
    if inbound_dnd_settings:
        payload["inboundDndSettings"] = inbound_dnd_settings
    if tags:
        payload["tags"] = tags
    if custom_fields:
        payload["customFields"] = custom_fields
    if source:
        payload["source"] = source
    if country:
        payload["country"] = country
    if company_name:
        payload["companyName"] = company_name
    if assigned_to:
        payload["assignedTo"] = assigned_to
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise