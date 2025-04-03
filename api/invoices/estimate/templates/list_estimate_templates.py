from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def list_estimate_templates(
    access_token: str,
    alt_id: str,
    alt_type: str = "location",
    limit: int = 10,
    offset: int = 0,
    search: Optional[str] = None
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/invoices/estimate/template"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION
    }
    
    params = {
        "altId": alt_id,
        "altType": alt_type,
        "limit": limit,
        "offset": offset
    }
    
    if search:
        params["search"] = search
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()