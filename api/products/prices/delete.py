from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_product_price(
    product_id: str,
    price_id: str,
    location_id: str,
    access_token: str
) -> Dict[str, bool]:
    """
    Delete a specific price associated with a particular product.

    Args:
        product_id: ID of the product
        price_id: ID of the price to delete
        location_id: ID of the location
        access_token: Access token for authentication

    Returns:
        Dictionary containing the deletion status

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/products/{product_id}/price/{price_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "locationId": location_id
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise Exception(f"Failed to delete product price: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred while deleting product price: {e}")