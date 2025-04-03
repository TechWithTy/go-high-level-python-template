from typing import Dict, Any, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-04-15"

async def enable_saas_for_sub_account(
    location_id: str,
    access_token: str,
    company_id: str,
    is_saas_v2: bool,
    stripe_account_id: Optional[str] = None,
    name: Optional[str] = None,
    email: Optional[str] = None,
    stripe_customer_id: Optional[str] = None,
    contact_id: Optional[str] = None,
    provider_location_id: Optional[str] = None,
    description: Optional[str] = None,
    saas_plan_id: Optional[str] = None,
    price_id: Optional[str] = None
) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "channel": "OAUTH",
        "source": "INTEGRATION",
        "Content-Type": "application/json"
    }

    payload = {
        "companyId": company_id,
        "isSaaSV2": is_saas_v2
    }

    if stripe_account_id:
        payload["stripeAccountId"] = stripe_account_id
    if name:
        payload["name"] = name
    if email:
        payload["email"] = email
    if stripe_customer_id:
        payload["stripeCustomerId"] = stripe_customer_id
    if contact_id:
        payload["contactId"] = contact_id
    if provider_location_id:
        payload["providerLocationId"] = provider_location_id
    if description:
        payload["description"] = description
    if saas_plan_id:
        payload["saasPlanId"] = saas_plan_id
    if price_id:
        payload["priceId"] = price_id

    url = f"{API_BASE_URL}/saas-api/public-api/enable-saas/{location_id}"

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()