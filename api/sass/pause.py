from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-04-15"

async def pause_sub_account(location_id: str, access_token: str, paused: bool, company_id: str) -> Dict[str, Any]:
    """
    Pause Sub account for given locationId.

    Args:
        location_id (str): The ID of the location to pause.
        access_token (str): The access token for authentication.
        paused (bool): Whether to pause the sub account.
        company_id (str): The ID of the company.

    Returns:
        Dict[str, Any]: The response from the API.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/saas-api/public-api/pause/{location_id}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "channel": "OAUTH",
        "source": "INTEGRATION",
        "Content-Type": "application/json"
    }
    
    data = {
        "paused": paused,
        "companyId": company_id
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()