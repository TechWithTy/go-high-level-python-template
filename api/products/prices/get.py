from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_price_by_id(
    product_id: str,
    price_id: str,
    location_id: str,
    access_token: str
) -> Dict[str, Any]:
    """
    Get Price by ID for a Product

    Args:
        product_id: ID of the product
        price_id: ID of the price
        location_id: ID of the location
        access_token: Access token for authentication

    Returns:
        Dictionary containing the price details

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/products/{product_id}/price/{price_id}"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION
    }

    params = {
        "locationId": location_id
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()