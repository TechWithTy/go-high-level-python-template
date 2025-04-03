import httpx
import logging
from typing import Dict, Any

async def verify_email(
    access_token: str,
    location_id: str,
    email: str,
    version: str = "2021-07-28"
) -> Dict[str, Any]:
    """
    Verify an email address using the Go High Level API.

    Args:
        access_token: The access token for authentication
        location_id: The location ID for billing purposes
        email: The email address to verify
        version: API version (default: "2021-07-28")

    Returns:
        Dictionary containing the email verification result

    Raises:
        Exception: If the API request fails
    """
    API_BASE_URL = "https://services.leadconnectorhq.com"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": version,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    params = {
        "locationId": location_id
    }

    payload = {
        "type": "email",
        "verify": email
    }

    logging.info(f"Verifying email: {email}")

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                f"{API_BASE_URL}/email/verify",
                headers=headers,
                params=params,
                json=payload
            )

        response.raise_for_status()
        return response.json()

    except httpx.HTTPStatusError as e:
        logging.error(f"API request failed with status {e.response.status_code}: {e.response.text}")
        raise Exception(f"API request failed: {str(e)}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise