from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_template_late_fees_config(
    template_id: str,
    alt_id: str,
    alt_type: str,
    late_fees_config: Dict[str, Any],
    access_token: str
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/invoices/template/{template_id}/late-fees-configuration"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }
    
    payload = {
        "altId": alt_id,
        "altType": alt_type,
        "lateFeesConfiguration": late_fees_config
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.patch(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()