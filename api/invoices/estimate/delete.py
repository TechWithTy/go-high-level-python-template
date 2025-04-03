import httpx
from typing import Dict, Any

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_invoice_estimate(access_token: str, estimate_id: str, alt_id: str, alt_type: str = "location") -> Dict[str, Any]:
    url = f"{API_BASE_URL}/invoices/estimate/{estimate_id}"
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