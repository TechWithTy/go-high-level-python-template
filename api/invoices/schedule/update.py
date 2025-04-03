import requests
from typing import List, Dict, Optional
from datetime import datetime

def update_schedule(schedule_id: str, access_token: str, alt_id: str, alt_type: str, name: str,
                    contact_details: Dict, schedule: Dict, live_mode: bool, business_details: Dict,
                    currency: str, items: List[Dict], discount: Optional[Dict] = None,
                    terms_notes: Optional[str] = None, title: Optional[str] = None,
                    attachments: Optional[List[Dict]] = None) -> Dict:
    url = f"https://services.leadconnectorhq.com/invoices/schedule/{schedule_id}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": "2021-07-28"
    }
    
    payload = {
        "altId": alt_id,
        "altType": alt_type,
        "name": name,
        "contactDetails": contact_details,
        "schedule": schedule,
        "liveMode": live_mode,
        "businessDetails": business_details,
        "currency": currency,
        "items": items
    }
    
    if discount:
        payload["discount"] = discount
    if terms_notes:
        payload["termsNotes"] = terms_notes
    if title:
        payload["title"] = title
    if attachments:
        payload["attachments"] = attachments
    
    response = requests.put(url, headers=headers, json=payload)
    response.raise_for_status()
    
    return response.json()