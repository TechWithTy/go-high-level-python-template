from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_survey_submissions(
    access_token: str,
    location_id: str,
    end_at: Optional[str] = None,
    limit: int = 20,
    page: int = 1,
    q: Optional[str] = None,
    start_at: Optional[str] = None,
    survey_id: Optional[str] = None
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/surveys/submissions"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION
    }
    
    params = {
        "locationId": location_id,
        "limit": str(limit),
        "page": str(page)
    }
    
    if end_at:
        params["endAt"] = end_at
    if q:
        params["q"] = q
    if start_at:
        params["startAt"] = start_at
    if survey_id:
        params["surveyId"] = survey_id

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
    
    response.raise_for_status()
    return response.json()