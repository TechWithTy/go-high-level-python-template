import requests

def create_user(access_token):
    url = "https://services.leadconnectorhq.com/users/"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": "2021-07-28"
    }

    response = requests.post(url, headers=headers)
    
    if response.status_code == 201:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"