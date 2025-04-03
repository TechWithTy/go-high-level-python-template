import requests

def update_user(access_token, user_id, user_data):
    url = f"https://services.leadconnectorhq.com/users/{user_id}"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": "2021-07-28"
    }
    
    response = requests.put(url, headers=headers, json=user_data)
    
    return response.json()