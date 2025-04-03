import requests

def create_invoice_estimate(access_token: str, payload: dict) -> dict:
    url = "https://services.leadconnectorhq.com/invoices/estimate"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Version": "2021-07-28"
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()