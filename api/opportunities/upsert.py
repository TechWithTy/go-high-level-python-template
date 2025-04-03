from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def upsert_opportunity(
    access_token: str,
    pipeline_id: str,
    location_id: str,
    contact_id: str,
    name: str,
    status: str,
    pipeline_stage_id: str,
    monetary_value: float,
    assigned_to: str
) -> Dict[str, Any]:
    """
    Upsert an opportunity in Go High Level API.

    Args:
        access_token: Bearer token for authentication
        pipeline_id: ID of the pipeline
        location_id: ID of the location
        contact_id: ID of the contact
        name: Name of the opportunity
        status: Status of the opportunity (open, won, lost, abandoned, all)
        pipeline_stage_id: ID of the pipeline stage
        monetary_value: Monetary value of the opportunity
        assigned_to: ID of the user the opportunity is assigned to

    Returns:
        Dictionary containing the upserted opportunity data

    Raises:
        Exception: If the API request fails
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = {
        "pipelineId": pipeline_id,
        "locationId": location_id,
        "contactId": contact_id,
        "name": name,
        "status": status,
        "pipelineStageId": pipeline_stage_id,
        "monetaryValue": monetary_value,
        "assignedTo": assigned_to
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{API_BASE_URL}/opportunities/upsert",
                headers=headers,
                json=data
            )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise Exception(f"Failed to upsert opportunity: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise Exception(f"An error occurred while upserting opportunity: {e}")