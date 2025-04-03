from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_snapshot_share_link(
    access_token: str,
    snapshot_id: str,
    share_type: str,
    company_id: str,
    relationship_number: Optional[str] = None,
    share_location_id: Optional[str] = None
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/snapshots/share/link"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    params = {"companyId": company_id}

    data = {
        "snapshot_id": snapshot_id,
        "share_type": share_type
    }

    if relationship_number:
        data["relationship_number"] = relationship_number
    if share_location_id:
        data["share_location_id"] = share_location_id

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()