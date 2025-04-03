from typing import Dict, Any, Optional
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def check_url_slug(
    token: str,
    location_id: str,
    url_slug: str,
    post_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Check if a blog post URL slug exists.

    Args:
        token: Access token for authentication
        location_id: ID of the location
        url_slug: URL slug to check
        post_id: Optional post ID

    Returns:
        Dictionary containing the API response

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/blogs/posts/url-slug-exists"

    headers = {
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION,
        "Accept": "application/json"
    }

    params = {
        "locationId": location_id,
        "urlSlug": url_slug
    }

    if post_id:
        params["postId"] = post_id

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise