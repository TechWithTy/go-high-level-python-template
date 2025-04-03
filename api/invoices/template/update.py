from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_invoice_template(
    template_id: str,
    access_token: str,
    data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Update an invoice template by template ID.

    Args:
        template_id (str): The ID of the template to update.
        access_token (str): The access token for authentication.
        data (Dict[str, Any]): The data to update the template with.

    Returns:
        Dict[str, Any]: The updated template data.

    Raises:
        httpx.HTTPStatusError: If the API request fails.
    """
    url = f"{API_BASE_URL}/invoices/template/{template_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.put(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()