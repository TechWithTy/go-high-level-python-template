from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_product_by_id(
    product_id: str,
    location_id: str,
    access_token: str
) -> Dict[str, Any]:
    """
    Get Product by ID

    Retrieves information for a specific product using its unique identifier.

    Args:
        product_id: ID of the product that needs to be returned
        location_id: Unique identifier for the location
        access_token: Access Token for authentication

    Returns:
        Dictionary containing the product details

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/products/{product_id}"

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