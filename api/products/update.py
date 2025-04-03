from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_product(
    product_id: str,
    product_data: Dict[str, Any],
    access_token: str
) -> Dict[str, Any]:
    """
    Update a product by ID using the Go High Level API.

    Args:
        product_id: The ID of the product to update
        product_data: Dictionary containing product details to update
        access_token: Access token for authentication

    Returns:
        Dictionary containing the updated product data

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/products/{product_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    logging.info(f"Updating product with ID: {product_id}")

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.put(url, headers=headers, json=product_data)

        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"API request failed with status {e.response.status_code}: {e.response.text}")
        raise Exception(f"Failed to update product: {e}")