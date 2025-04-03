from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def fetch_redirect_list(
    token: str,
    location_id: str,
    limit: int = 20,
    offset: int = 0,
    search: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieves a list of all URL redirects based on the given query parameters.

    Args:
        token: The access token for authentication
        location_id: The location ID
        limit: Maximum number of results to return (default: 20)
        offset: Number of results to skip (default: 0)
        search: Optional search string

    Returns:
        Dictionary containing the count of redirects and an array of redirect data
    """
    url = f"{API_BASE_URL}/funnels/lookup/redirect/list"

    headers = {
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "locationId": location_id,
        "limit": limit,
        "offset": offset
    }

    if search:
        params["search"] = search

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()