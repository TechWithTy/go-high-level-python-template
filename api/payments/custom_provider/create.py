from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_custom_provider(
    access_token: str,
    location_id: str,
    name: str,
    description: str,
    payments_url: str,
    query_url: str,
    image_url: str
) -> Dict[str, Any]:
    """
    Create a new custom payment provider integration.

    Args:
        access_token (str): The access token for authentication.
        location_id (str): The location ID.
        name (str): The name of the custom provider.
        description (str): Description of the payment gateway.
        payments_url (str): URL for starting a payment session.
        query_url (str): URL for querying payments related events.
        image_url (str): Public image URL for the payment gateway logo.

    Returns:
        Dict[str, Any]: The response data from the API.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/payments/custom-provider/provider"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    params = {
        "locationId": location_id
    }

    data = {
        "name": name,
        "description": description,
        "paymentsUrl": payments_url,
        "queryUrl": query_url,
        "imageUrl": image_url
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()

    return response.json()