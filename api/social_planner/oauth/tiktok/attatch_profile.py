from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def attach_tiktok_profile(
    access_token: str,
    location_id: str,
    account_id: str,
    profile_type: str,
    origin_id: str,
    name: str,
    avatar: str,
    verified: bool,
    username: str,
    company_id: str
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/social-media-posting/oauth/{location_id}/tiktok/accounts/{account_id}"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }

    data = {
        "type": profile_type,
        "originId": origin_id,
        "name": name,
        "avatar": avatar,
        "verified": verified,
        "username": username,
        "companyId": company_id
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()