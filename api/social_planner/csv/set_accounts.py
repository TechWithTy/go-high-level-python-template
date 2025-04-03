from typing import Dict, Any, List
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def set_accounts(
    access_token: str,
    location_id: str,
    account_ids: List[str],
    file_path: str,
    rows_count: int,
    file_name: str,
    approver: str = None,
    user_id: str = None
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/set-accounts"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }

    data = {
        "accountIds": account_ids,
        "filePath": file_path,
        "rowsCount": rows_count,
        "fileName": file_name
    }

    if approver:
        data["approver"] = approver
    if user_id:
        data["userId"] = user_id

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()