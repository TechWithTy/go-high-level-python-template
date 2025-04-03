import httpx
from typing import Dict, Any

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def schedule_invoice(
    schedule_id: str,
    access_token: str,
    alt_id: str,
    alt_type: str = "location",
    live_mode: bool = True,
    auto_payment: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Schedule an invoice to start sending to the customer.

    Args:
        schedule_id: The ID of the schedule
        access_token: The bearer token for authentication
        alt_id: Location ID or company ID based on altType
        alt_type: Alt Type, defaults to "location"
        live_mode: Whether to use live mode, defaults to True
        auto_payment: Auto-payment configuration, optional

    Returns:
        Dictionary containing the scheduled invoice data

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/invoices/schedule/{schedule_id}/schedule"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "altId": alt_id,
        "altType": alt_type,
        "liveMode": live_mode
    }

    if auto_payment:
        payload["autoPayment"] = auto_payment

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()