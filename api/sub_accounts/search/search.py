from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def search_sub_accounts(
    access_token: str,
    company_id: Optional[str] = None,
    email: Optional[str] = None,
    limit: int = 10,
    order: str = "asc",
    skip: int = 0
) -> Dict[str, Any]:
    """
    Search Sub-Accounts (Formerly Locations)

    Args:
        access_token: Access Token for authentication
        company_id: The company/agency id on which to perform the search
        email: Email to search for
        limit: The value by which the results should be limited (default: 10)
        order: The order in which the results should be returned (asc or desc, default: asc)
        skip: The value by which the results should be skipped (default: 0)

    Returns:
        Dict containing the search results
    """
    url = f"{API_BASE_URL}/locations/search"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION
    }

    params = {
        "companyId": company_id,
        "email": email,
        "limit": limit,
        "order": order,
        "skip": skip
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()