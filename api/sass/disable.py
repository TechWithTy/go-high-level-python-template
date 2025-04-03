from typing import Dict, Any, List
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-04-15"

async def disable_saas_for_locations(
    access_token: str,
    company_id: str,
    location_ids: List[str]
) -> Dict[str, Any]:
    """
    Disable SaaS for locations for given locationIds.

    Args:
        access_token: Access Token for authentication
        company_id: The company ID
        location_ids: List of location IDs to disable SaaS for

    Returns:
        Dict containing the API response
    """
    url = f"{API_BASE_URL}/saas-api/public-api/bulk-disable-saas/{company_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION,
        "channel": "OAUTH",
        "source": "INTEGRATION"
    }

    data = {"locationIds": location_ids}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()