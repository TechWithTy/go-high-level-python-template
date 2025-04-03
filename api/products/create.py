from typing import Dict, Any
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_product(
    access_token: str,
    name: str,
    location_id: str,
    product_type: str,
    description: str = None,
    image: str = None,
    statement_descriptor: str = None,
    available_in_store: bool = None,
    medias: list = None,
    variants: list = None
) -> Dict[str, Any]:
    url = f"{API_BASE_URL}/products/"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }
    
    payload = {
        "name": name,
        "locationId": location_id,
        "productType": product_type
    }
    
    if description:
        payload["description"] = description
    if image:
        payload["image"] = image
    if statement_descriptor:
        payload["statementDescriptor"] = statement_descriptor
    if available_in_store is not None:
        payload["availableInStore"] = available_in_store
    if medias:
        payload["medias"] = medias
    if variants:
        payload["variants"] = variants
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
    
    response.raise_for_status()
    return response.json()