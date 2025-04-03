from typing import Dict, Any
import httpx
import logging

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def update_blog_post(
    post_id: str,
    blog_data: Dict[str, Any],
    access_token: str
) -> Dict[str, Any]:
    """
    Update a blog post using the Go High Level API.

    Args:
        post_id: The ID of the blog post to update
        blog_data: Dictionary containing blog post details to update
        access_token: Access token for authentication

    Returns:
        Dictionary containing the updated blog post data

    Raises:
        Exception: If the API request fails
    """
    url = f"{API_BASE_URL}/blogs/posts/{post_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": API_VERSION,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    logging.info(f"Updating blog post with ID: {post_id}")

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.put(url, headers=headers, json=blog_data)

        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"API request failed with status {e.response.status_code}: {e.response.text}")
        raise Exception(f"Failed to update blog post: {e}")