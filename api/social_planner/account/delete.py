from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_social_media_account(
    access_token: str,
    location_id: str,
    account_id: str,
    company_id: Optional[str] = None,
    user_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Delete a social media account and remove it from the group.

    Args:
        access_token: The access token for authentication
        location_id: The ID of the location
        account_id: The ID of the account to delete
        company_id: Optional company ID
        user_id: Optional user ID

    Returns:
        Dictionary containing the API response

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/social-media-posting/{location_id}/accounts/{account_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {}
    if company_id:
        params["companyId"] = company_id
    if user_id:
        params["userId"] = user_id

    async with httpx.AsyncClient() as client:
        response = await client.delete(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()