from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def list_product_prices(
    product_id: str,
    location_id: str,
    access_token: str,
    ids: Optional[str] = None,
    limit: Optional[int] = 0,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    List Prices for a Product

    Args:
        product_id: ID of the product
        location_id: The unique identifier for the location
        access_token: Access token for authentication
        ids: Comma-separated price IDs to filter the response
        limit: The maximum number of items per page (default: 0)
        offset: The starting index of the page (default: 0)

    Returns:
        Dictionary containing the list of prices and total count

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/products/{product_id}/price"

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

    if ids:
        params["ids"] = ids

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()