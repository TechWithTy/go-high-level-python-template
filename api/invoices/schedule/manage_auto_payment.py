import requests
from typing import Dict, Any

def manage_auto_payment(schedule_id: str, alt_id: str, alt_type: str, auto_payment: Dict[str, Any], token: str) -> Dict[str, Any]:
    url = f"https://services.leadconnectorhq.com/invoices/schedule/{schedule_id}/auto-payment"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Version": "2021-07-28",
        "Content-Type": "application/json"
    }
    
    payload = {
        "altId": alt_id,
        "altType": alt_type,
        "id": schedule_id,
        "autoPayment": auto_payment
    }
    
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    
    return response.json()