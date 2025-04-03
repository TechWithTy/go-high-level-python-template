from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def delete_redirect_by_id(
    redirect_id: str,
    location_id: str,
    access_token: str
) -> Dict[str, Any]:
    """
    Delete a URL redirect by its ID.

    Args:
        redirect_id: The ID of the redirect to delete
        location_id: The location ID
        access_token: The access token for authentication

    Returns:
        A dictionary containing the status of the delete operation
    """
    url = f"{API_BASE_URL}/funnels/lookup/redirect/{redirect_id}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }
    
    params = {
        "locationId": location_id
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.delete(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()