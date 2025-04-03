from typing import Dict, Any, List
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def add_followers(
    opportunity_id: str,
    followers: List[str],
    auth_token: str
) -> Dict[str, Any]:
    """
    Add followers to an opportunity in Go High Level.
    
    Args:
        opportunity_id: The ID of the opportunity to add followers to
        followers: List of follower IDs to add to the opportunity
        auth_token: Bearer token for authentication
        
    Returns:
        Dictionary containing the response data with followers and followersAdded
    """
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "followers": followers
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{API_BASE_URL}/opportunities/{opportunity_id}/followers",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        logging.error(f"Error adding followers to opportunity {opportunity_id}: {str(e)}")
        raise