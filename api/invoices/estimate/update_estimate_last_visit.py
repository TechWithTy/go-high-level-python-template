from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_estimate_last_visited(access_token: str, estimate_id: str) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/invoices/estimate/stats/last-visited-at"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }
    data = {"estimateId": estimate_id}

    async with httpx.AsyncClient() as client:
        response = await client.patch(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()