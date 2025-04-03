from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-04-15"

async def update_saas_subscription(
    location_id: str,
    access_token: str,
    subscription_id: str,
    customer_id: str,
    company_id: str
) -> Dict[str, Any]:
    """
    Update SaaS subscription for given locationId and customerId.

    Args:
        location_id (str): The ID of the location.
        access_token (str): The access token for authentication.
        subscription_id (str): The ID of the subscription to update.
        customer_id (str): The ID of the customer.
        company_id (str): The ID of the company.

    Returns:
        Dict[str, Any]: The response from the API.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/saas-api/public-api/update-saas-subscription/{location_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION,
        "channel": "OAUTH",
        "source": "INTEGRATION"
    }

    data = {
        "subscriptionId": subscription_id,
        "customerId": customer_id,
        "companyId": company_id
    }

    async with httpx.AsyncClient() as client:
        response = await client.put(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()