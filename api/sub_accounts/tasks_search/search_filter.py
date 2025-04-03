from typing import Dict, Any, List, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def search_tasks(
    location_id: str,
    access_token: str,
    contact_ids: Optional[List[str]] = None,
    completed: Optional[bool] = None,
    assigned_to: Optional[List[str]] = None,
    query: Optional[str] = None,
    limit: int = 25,
    skip: int = 0,
    business_id: Optional[str] = None
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/locations/{location_id}/tasks/search"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {}
    if contact_ids:
        payload["contactId"] = contact_ids
    if completed is not None:
        payload["completed"] = completed
    if assigned_to:
        payload["assignedTo"] = assigned_to
    if query:
        payload["query"] = query
    if limit != 25:
        payload["limit"] = limit
    if skip != 0:
        payload["skip"] = skip
    if business_id:
        payload["businessId"] = business_id

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()