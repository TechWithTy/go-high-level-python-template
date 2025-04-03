from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def send_estimate(
    access_token: str,
    estimate_id: str,
    alt_id: str,
    alt_type: str = "location",
    action: str = "sms_and_email",
    live_mode: bool = True,
    user_id: str = None,
    from_name: str = None,
    from_email: str = None,
    estimate_name: str = "Estimate"
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/invoices/estimate/{estimate_id}/send"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }

    data = {
        "altId": alt_id,
        "altType": alt_type,
        "action": action,
        "liveMode": live_mode,
        "userId": user_id,
        "sentFrom": {
            "fromName": from_name,
            "fromEmail": from_email
        },
        "estimateName": estimate_name
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()