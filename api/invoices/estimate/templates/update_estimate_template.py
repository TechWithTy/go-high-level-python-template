import requests

def update_estimate_template(access_token, template_id, payload):
    url = f"https://services.leadconnectorhq.com/invoices/estimate/template/{template_id}"
    
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": "2021-07-28"
    }
    
    response = requests.put(url, headers=headers, json=payload)
    
    return response.json()