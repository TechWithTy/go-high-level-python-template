import requests
from typing import List, Dict, Optional
from datetime import datetime

def create_invoice_schedule(
    access_token: str,
    alt_id: str,
    alt_type: str,
    name: str,
    contact_details: Dict,
    schedule: Dict,
    live_mode: bool,
    business_details: Dict,
    currency: str,
    items: List[Dict],
    automatic_taxes_enabled: bool,
    discount: Dict,
    terms_notes: str,
    title: str,
    tips_configuration: Dict,
    late_fees_configuration: Dict,
    invoice_number_prefix: str,
    payment_methods: Dict,
    attachments: List[Dict]
) -> Dict:
    url = "https://services.leadconnectorhq.com/invoices/schedule"
    
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
        "items": items,
        "automaticTaxesEnabled": automatic_taxes_enabled,
        "discount": discount,
        "termsNotes": terms_notes,
        "title": title,
        "tipsConfiguration": tips_configuration,
        "lateFeesConfiguration": late_fees_configuration,
        "invoiceNumberPrefix": invoice_number_prefix,
        "paymentMethods": payment_methods,
        "attachments": attachments
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()