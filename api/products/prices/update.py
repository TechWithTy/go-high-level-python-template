from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_product_price(
    product_id: str,
    price_id: str,
    price_data: Dict[str, Any],
    access_token: str
) -> Dict[str, Any]:
    """
    Update Price by ID for a Product.

    Args:
        product_id: ID of the product
        price_id: ID of the price to update
        price_data: Dictionary containing price details to update
        access_token: Access token for authentication

    Returns:
        Dictionary containing the updated price data

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/products/{product_id}/price/{price_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    logging.info(f"Updating price with ID: {price_id} for product: {product_id}")

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.put(url, headers=headers, json=price_data)

        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"API request failed with status {e.response.status_code}: {e.response.text}")
        raise Exception(f"Failed to update product price: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred while updating product price: {e}")