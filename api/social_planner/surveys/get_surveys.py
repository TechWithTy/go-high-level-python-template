from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_surveys(
    access_token: str,
    location_id: str,
    limit: Optional[int] = 10,
    skip: Optional[int] = 0,
    survey_type: Optional[str] = None
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/surveys/"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }
    
    params = {
        "locationId": location_id,
        "limit": limit,
        "skip": skip
    }
    
    if survey_type:
        params["type"] = survey_type

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()