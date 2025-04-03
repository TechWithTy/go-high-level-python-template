from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_templates(
    location_id: str,
    access_token: str,
    origin_id: str,
    deleted: bool = False,
    limit: int = 25,
    skip: int = 0,
    template_type: Optional[str] = None
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/locations/{location_id}/templates"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "originId": origin_id,
        "deleted": str(deleted).lower(),
        "limit": str(limit),
        "skip": str(skip)
    }

    if template_type:
        params["type"] = template_type

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()