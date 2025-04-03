from typing import Dict, Any, List
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def remove_opportunity_followers(
    opportunity_id: str,
    followers: List[str],
    access_token: str
) -> Dict[str, Any]:
    """
    Remove followers from an opportunity.

    Args:
        opportunity_id: The ID of the opportunity
        followers: List of follower IDs to remove
        access_token: The access token for authentication

    Returns:
        Dictionary containing the API response

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/opportunities/{opportunity_id}/followers"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=headers, json={"followers": followers})
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise Exception(f"Failed to remove opportunity followers: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred while removing opportunity followers: {e}")