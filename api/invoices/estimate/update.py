import httpx
from typing import Dict, Any

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_estimate(
    estimate_id: str,
    access_token: str,
    data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Update an existing estimate with new details.

    Args:
        estimate_id: The ID of the estimate to update
        access_token: The access token for authentication
        data: The estimate data to update

    Returns:
        Dictionary containing the updated estimate data

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/invoices/estimate/{estimate_id}"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }

    async with httpx.AsyncClient() as client:
        response = await client.put(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()