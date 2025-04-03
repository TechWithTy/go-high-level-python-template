import requests
import json
from typing import Dict, List, Any, Optional


def create_invoice(
    access_token: str,
    alt_id: str,
    name: str,
    contact_id: str,
    contact_name: str,
    issue_date: str,
    items: List[Dict[str, Any]],
    currency: str = "USD",
    alt_type: str = "location",
    business_details: Optional[Dict[str, Any]] = None,
    discount: Optional[Dict[str, Any]] = None,
    terms_notes: Optional[str] = None,
    title: str = "INVOICE",
    contact_details: Optional[Dict[str, Any]] = None,
    invoice_number: Optional[str] = None,
    due_date: Optional[str] = None,
    sent_to: Optional[Dict[str, List[str]]] = None,
    live_mode: bool = True,
    automatic_taxes_enabled: bool = False,
    payment_schedule: Optional[Dict[str, Any]] = None,
    late_fees_config: Optional[Dict[str, Any]] = None,
    tips_config: Optional[Dict[str, Any]] = None,
    invoice_number_prefix: Optional[str] = None,
    payment_methods: Optional[Dict[str, Any]] = None,
    attachments: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """
    Create an invoice using GoHighLevel API
    
    Args:
        access_token: Bearer token for authentication
        alt_id: Location ID or company ID
        name: Invoice name
        contact_id: Contact ID
        contact_name: Contact name
        issue_date: Issue date in YYYY-MM-DD format
        items: List of invoice items
        currency: Currency code (default: USD)
        alt_type: Alt type (default: location)
        business_details: Business details
        discount: Discount information
        terms_notes: Terms and notes
        title: Invoice title
        contact_details: Additional contact details
        invoice_number: Invoice number
        due_date: Due date in YYYY-MM-DD format
        sent_to: Email and phone recipients
        live_mode: Live mode flag
        automatic_taxes_enabled: Enable automatic taxes
        payment_schedule: Payment schedule details
        late_fees_config: Late fees configuration
        tips_config: Tips configuration
        invoice_number_prefix: Prefix for invoice number
        payment_methods: Payment methods configuration
        attachments: List of attachments
    
    Returns:
        API response as dictionary
    """
    url = "https://services.leadconnectorhq.com/invoices/"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": "2021-07-28",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # Prepare minimal required contact details
    if contact_details is None:
        contact_details = {
            "id": contact_id,
            "name": contact_name
        }
    
    # Prepare minimal required payload
    payload = {
        "altId": alt_id,
        "altType": alt_type,
        "name": name,
        "currency": currency,
        "items": items,
        "contactDetails": contact_details,
        "issueDate": issue_date,
        "title": title,
        "liveMode": live_mode
    }
    
    # Add optional fields if provided
    if business_details:
        payload["businessDetails"] = business_details
    if discount:
        payload["discount"] = discount
    if terms_notes:
        payload["termsNotes"] = terms_notes
    if invoice_number:
        payload["invoiceNumber"] = invoice_number
    if due_date:
        payload["dueDate"] = due_date
    if sent_to:
        payload["sentTo"] = sent_to
    if automatic_taxes_enabled:
        payload["automaticTaxesEnabled"] = automatic_taxes_enabled
    if payment_schedule:
        payload["paymentSchedule"] = payment_schedule
    if late_fees_config:
        payload["lateFeesConfiguration"] = late_fees_config
    if tips_config:
        payload["tipsConfiguration"] = tips_config
    if invoice_number_prefix:
        payload["invoiceNumberPrefix"] = invoice_number_prefix
    if payment_methods:
        payload["paymentMethods"] = payment_methods
    if attachments:
        payload["attachments"] = attachments
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()