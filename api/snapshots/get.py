from typing import Dict, Any, List
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_snapshots(access_token: str, company_id: str) -> List[Dict[str, Any]]:
    """
    Get a list of all own and imported Snapshots.

    Args:
        access_token (str): The access token for authentication.
        company_id (str): The company ID.

    Returns:
        List[Dict[str, Any]]: A list of snapshot dictionaries.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/snapshots/"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION
    }
    
    params = {
        "companyId": company_id
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()["snapshots"]