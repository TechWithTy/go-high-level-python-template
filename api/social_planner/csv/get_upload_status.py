from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_upload_status(
    access_token: str,
    location_id: str,
    include_users: Optional[bool] = None,
    limit: int = 10,
    skip: int = 0,
    user_id: Optional[str] = None
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/csv"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION
    }

    params = {
        "limit": str(limit),
        "skip": str(skip)
    }

    if include_users is not None:
        params["includeUsers"] = str(include_users).lower()
    if user_id:
        params["userId"] = user_id

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()