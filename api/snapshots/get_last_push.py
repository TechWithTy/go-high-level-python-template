import httpx
from typing import Dict, Any

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_last_snapshot_push(
    access_token: str,
    location_id: str,
    snapshot_id: str,
    company_id: str
) -> Dict[str, Any]:
    """
    Get Latest Snapshot Push Status for a location id.

    Args:
        access_token (str): The access token for authentication.
        location_id (str): The ID of the location.
        snapshot_id (str): The ID of the snapshot.
        company_id (str): The ID of the company.

    Returns:
        Dict[str, Any]: The API response containing snapshot push status.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/snapshots/snapshot-status/{snapshot_id}/location/{location_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {"companyId": company_id}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()