from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_redirect(
    token: str,
    location_id: str,
    domain: str,
    path: str,
    target: str,
    action: str
) -> Dict[str, Any]:
    """
    Create a new URL redirect in the system.

    Args:
        token: Access token for authentication
        location_id: Identifier of the location associated with the redirect
        domain: Domain where the redirect occurs
        path: Original path that will be redirected
        target: Target URL to which the original path will be redirected
        action: Action performed by the redirect (e.g., 'funnel', 'website', 'url', 'all')

    Returns:
        Dict containing details of the created redirect

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/funnels/lookup/redirect"

    headers = {
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = {
        "locationId": location_id,
        "domain": domain,
        "path": path,
        "target": target,
        "action": action
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()