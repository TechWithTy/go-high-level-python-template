import requests

def edit_post(access_token, location_id, post_id, payload):
    url = f"https://services.leadconnectorhq.com/social-media-posting/{location_id}/posts/{post_id}"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": "2021-07-28"
    }
    
    response = requests.put(url, headers=headers, json=payload)
    return response.json()