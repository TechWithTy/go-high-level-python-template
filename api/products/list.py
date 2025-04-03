from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def list_products(
    access_token: str,
    location_id: str,
    limit: Optional[int] = 0,
    offset: Optional[int] = 0,
    search: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve a paginated list of products.

    Args:
        access_token: The access token for authentication.
        location_id: The ID of the sub-account location.
        limit: The maximum number of items per page (default: 0).
        offset: The starting index of the page (default: 0).
        search: The name of the product to search for (optional).

    Returns:
        A dictionary containing the list of products and total count.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/products/"

    headers = {
        "Authorization": f"Bearer {access_token}",
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