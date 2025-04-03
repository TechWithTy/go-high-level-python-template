import httpx
from typing import Dict, Any

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_template_payment_method_config(
    template_id: str,
    alt_id: str,
    alt_type: str,
    enable_bank_debit_only: bool,
    access_token: str
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/invoices/template/{template_id}/payment-methods-configuration"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }
    
    payload = {
        "altId": alt_id,
        "altType": alt_type,
        "paymentMethods": {
            "stripe": {
                "enableBankDebitOnly": enable_bank_debit_only
            }
        }
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.patch(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()