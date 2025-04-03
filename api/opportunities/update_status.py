from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_opportunity_status(
    opportunity_id: str,
    status: str,
    access_token: str
) -> Dict[str, Any]:
    """
    Update the status of an opportunity in Go High Level.

    Args:
        opportunity_id: The ID of the opportunity to update
        status: The new status of the opportunity (open, won, lost, abandoned, or all)
        access_token: The access token for authentication

    Returns:
        Dictionary containing the API response

    Raises:
        Exception: If the API request fails
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = {"status": status}

    logging.info(f"Updating status for opportunity: {opportunity_id}")

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.put(
                f"{API_BASE_URL}/opportunities/{opportunity_id}/status",
                headers=headers,
                json=data
            )

        response.raise_for_status()
        return response.json()

    except httpx.HTTPStatusError as e:
        logging.error(f"API request failed with status {e.response.status_code}: {e.response.text}")
        raise Exception(f"Failed to update opportunity status: {e}")