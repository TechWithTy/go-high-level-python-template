from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_user(user_id: str, access_token: str) -> Dict[str, Any]:
    """
    Get user details from the Go High Level API.

    Args:
        user_id (str): The ID of the user to retrieve.
        access_token (str): The access token for authentication.

    Returns:
        Dict[str, Any]: The user details.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/users/{user_id}", headers=headers)
        response.raise_for_status()
        return response.json()