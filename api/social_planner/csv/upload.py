from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def upload_csv(access_token: str, location_id: str, file_path: str) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/csv"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION
    }

    async with httpx.AsyncClient() as client:
        with open(file_path, "rb") as file:
            files = {"file": file}
            response = await client.post(url, headers=headers, files=files)

    response.raise_for_status()
    return response.json()