from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_categories_by_location_id(
    access_token: str,
    location_id: str,
    limit: Optional[int] = None,
    search_text: Optional[str] = None,
    skip: Optional[int] = None
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/categories"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {}
    if limit:
        params["limit"] = limit
    if search_text:
        params["searchText"] = search_text
    if skip:
        params["skip"] = skip

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()