from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def fetch_funnel_page_count(
    access_token: str,
    funnel_id: str,
    location_id: str,
    name: Optional[str] = None
) -> Dict[str, Any]:
    """
    Fetch count of funnel pages.

    Args:
        access_token: The access token for authentication
        funnel_id: The ID of the funnel
        location_id: The ID of the location
        name: Optional name parameter for filtering

    Returns:
        Dictionary containing the count of funnel pages

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/funnels/page/count"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "funnelId": funnel_id,
        "locationId": location_id
    }

    if name:
        params["name"] = name

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()