from typing import Dict, Any, List
import httpx

API_BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

async def create_custom_menu(
    access_token: str,
    title: str,
    url: str,
    icon_name: str,
    icon_font_family: str,
    show_on_company: bool = True,
    show_on_location: bool = True,
    show_to_all_locations: bool = True,
    open_mode: str = "iframe",
    locations: List[str] = None,
    user_role: str = "all",
    allow_camera: bool = False,
    allow_microphone: bool = False
) -> Dict[str, Any]:
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": API_VERSION
    }

    data = {
        "title": title,
        "url": url,
        "icon": {
            "name": icon_name,
            "fontFamily": icon_font_family
        },
        "showOnCompany": show_on_company,
        "showOnLocation": show_on_location,
        "showToAllLocations": show_to_all_locations,
        "openMode": open_mode,
        "locations": locations or [],
        "userRole": user_role,
        "allowCamera": allow_camera,
        "allowMicrophone": allow_microphone
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/custom-menus/", headers=headers, json=data)
        response.raise_for_status()
        return response.json()