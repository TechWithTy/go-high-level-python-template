from typing import Dict, Any
import httpx
import json

async def update_sub_account(
    location_id: str,
    access_token: str,
    sub_account_data: Dict[str, Any],
    api_version: str = "2021-07-28"
) -> Dict[str, Any]:
    """
    Update a Sub-Account (Formerly Location) based on the data provided.

    Args:
        location_id (str): The ID of the location to update.
        access_token (str): The access token for authentication.
        sub_account_data (Dict[str, Any]): The data to update the sub-account with.
        api_version (str, optional): The API version to use. Defaults to "2021-07-28".

    Returns:
        Dict[str, Any]: The updated sub-account data.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"https://services.leadconnectorhq.com/locations/{location_id}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": api_version,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.put(url, headers=headers, json=sub_account_data)
        response.raise_for_status()
        return response.json()