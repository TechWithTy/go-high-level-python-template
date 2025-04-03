from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_link(
    link_id: str,
    name: str,
    redirect_to: str,
    access_token: str
) -> Dict[str, Any]:
    """
    Update a link in Go High Level.

    Args:
        link_id: The ID of the link to update
        name: New name for the link
        redirect_to: New redirect URL for the link
        access_token: The access token for authentication

    Returns:
        Dictionary containing the updated link data

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/links/{link_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    data = {
        "name": name,
        "redirectTo": redirect_to
    }

    async with httpx.AsyncClient() as client:
        response = await client.put(url, headers=headers, json=data)

        if response.status_code != 201:
            logging.error(f"Failed to update link: {response.text}")
            response.raise_for_status()

        return response.json()