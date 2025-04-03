from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_estimate_template(
    access_token: str,
    template_id: str,
    alt_id: str,
    alt_type: str = "location"
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/invoices/estimate/template/{template_id}"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION
    }
    
    params = {
        "altId": alt_id,
        "altType": alt_type
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.delete(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()