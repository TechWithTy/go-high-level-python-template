import httpx
from typing import Dict, Any, Optional

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_scheduled_invoice(
    schedule_id: str,
    access_token: str,
    data: Dict[str, Any],
    headers: Optional[Dict[str, str]] = None
) -> Dict[str, Any]:
    """
    Update scheduled recurring invoice.

    Args:
        schedule_id: The ID of the schedule to update
        access_token: The access token for authentication
        data: The invoice data to update
        headers: Optional additional headers

    Returns:
        Dictionary containing the updated invoice data

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/invoices/schedule/{schedule_id}/updateAndSchedule"

    default_headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }

    if headers:
        default_headers.update(headers)

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=default_headers, json=data)
        response.raise_for_status()
        return response.json()