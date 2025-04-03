from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"

async def fetch_funnel_pages(
    access_token: str,
    funnel_id: str,
    location_id: str,
    limit: int,
    offset: int,
    name: Optional[str] = None
) -> Dict[str, Any]:
    """
    Fetch list of funnel pages from the Go High Level API.

    Args:
        access_token: The access token for authentication
        funnel_id: The ID of the funnel
        location_id: The ID of the location
        limit: Maximum number of pages to return
        offset: Number of pages to skip
        name: Optional name filter for pages

    Returns:
        Dictionary containing the funnel pages data

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }

    params = {
        "funnelId": funnel_id,
        "locationId": location_id,
        "limit": limit,
        "offset": offset
    }

    if name:
        params["name"] = name

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_BASE_URL}/funnels/page",
            headers=headers,
            params=params
        )
        response.raise_for_status()
        return response.json()