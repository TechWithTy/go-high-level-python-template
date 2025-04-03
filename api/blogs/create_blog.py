import httpx
from typing import Dict, Any

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_blog_post(
    access_token: str,
    title: str,
    location_id: str,
    blog_id: str,
    image_url: str,
    description: str,
    raw_html: str,
    status: str,
    image_alt_text: str,
    categories: list,
    tags: list,
    author: str,
    url_slug: str,
    canonical_link: str,
    published_at: str
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/blogs/posts"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }
    
    payload = {
        "title": title,
        "locationId": location_id,
        "blogId": blog_id,
        "imageUrl": image_url,
        "description": description,
        "rawHTML": raw_html,
        "status": status,
        "imageAltText": image_alt_text,
        "categories": categories,
        "tags": tags,
        "author": author,
        "urlSlug": url_slug,
        "canonicalLink": canonical_link,
        "publishedAt": published_at
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
    
    response.raise_for_status()
    return response.json()