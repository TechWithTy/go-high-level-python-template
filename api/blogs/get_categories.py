from typing import Dict, Any, Optional
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def get_blog_categories(
    location_id: str,
    access_token: str,
    limit: int = 10,
    offset: int = 0
) -> Dict[str, Any]:
    """
    Get all blog categories for a given location ID.

    Args:
        location_id: The ID of the location to fetch categories for
        access_token: The access token for authentication
        limit: Number of categories to show in the listing (default: 10)
        offset: Number of categories to skip in listing (default: 0)

    Returns:
        Dictionary containing the blog categories data

    Raises:
        httpx.HTTPStatusError: If the API request fails
    """
    url = f"{API_BASE_URL}/blogs/categories"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "locationId": location_id,
        "limit": limit,
        "offset": offset
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()