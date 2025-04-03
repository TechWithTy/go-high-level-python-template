from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_custom_menu_links(
    access_token: str,
    limit: Optional[int] = 20,
    location_id: Optional[str] = None,
    query: Optional[str] = None,
    show_on_company: Optional[bool] = None,
    skip: Optional[int] = 0
) -> Dict[str, Any]:
    """
    Fetches a collection of custom menus based on specified criteria.

    Args:
        access_token (str): The access token for authentication.
        limit (int, optional): Maximum number of items to return. Defaults to 20.
        location_id (str, optional): Unique identifier of the location.
        query (str, optional): Search query to filter custom menus by name.
        show_on_company (bool, optional): Filter to show only agency-level menu links.
        skip (int, optional): Number of items to skip for pagination. Defaults to 0.

    Returns:
        Dict[str, Any]: A dictionary containing the custom menu links data.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/custom-menus/"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "limit": limit,
        "locationId": location_id,
        "query": query,
        "showOnCompany": show_on_company,
        "skip": skip
    }

    params = {k: v for k, v in params.items() if v is not None}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()