from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-04-15"

async def get_location_stripe_id(
    access_token: str,
    company_id: str,
    customer_id: Optional[str] = None,
    subscription_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get locations by stripeId with companyId.

    Args:
        access_token (str): The access token for authentication.
        company_id (str): The ID of the company.
        customer_id (str, optional): The Stripe customer ID.
        subscription_id (str, optional): The Stripe subscription ID.

    Returns:
        Dict[str, Any]: The API response containing location information.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "channel": "OAUTH",
        "source": "INTEGRATION"
    }

    params = {"companyId": company_id}
    if customer_id:
        params["customerId"] = customer_id
    if subscription_id:
        params["subscriptionId"] = subscription_id

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_BASE_URL}/saas-api/public-api/locations",
            headers=headers,
            params=params
        )
        response.raise_for_status()
        return response.json()