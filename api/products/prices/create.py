import aiohttp
import json
from typing import Dict, Any, Optional

async def create_price_for_product(
    product_id: str,
    access_token: str,
    name: str,
    price_type: str,
    currency: str,
    amount: float,
    location_id: str,
    recurring: Optional[Dict[str, Any]] = None,
    description: Optional[str] = None,
    membership_offers: Optional[list] = None,
    trial_period: Optional[int] = None,
    total_cycles: Optional[int] = None,
    setup_fee: Optional[float] = None,
    variant_option_ids: Optional[list] = None,
    compare_at_price: Optional[float] = None,
    user_id: Optional[str] = None,
    meta: Optional[Dict[str, Any]] = None,
    track_inventory: Optional[bool] = None,
    available_quantity: Optional[int] = None,
    allow_out_of_stock_purchases: Optional[bool] = None
) -> Dict[str, Any]:
    url = f"https://services.leadconnectorhq.com/products/{product_id}/price"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": "2021-07-28",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "name": name,
        "type": price_type,
        "currency": currency,
        "amount": amount,
        "locationId": location_id
    }

    if recurring:
        payload["recurring"] = recurring
    if description:
        payload["description"] = description
    if membership_offers:
        payload["membershipOffers"] = membership_offers
    if trial_period is not None:
        payload["trialPeriod"] = trial_period
    if total_cycles is not None:
        payload["totalCycles"] = total_cycles
    if setup_fee is not None:
        payload["setupFee"] = setup_fee
    if variant_option_ids:
        payload["variantOptionIds"] = variant_option_ids
    if compare_at_price is not None:
        payload["compareAtPrice"] = compare_at_price
    if user_id:
        payload["userId"] = user_id
    if meta:
        payload["meta"] = meta
    if track_inventory is not None:
        payload["trackInventory"] = track_inventory
    if available_quantity is not None:
        payload["availableQuantity"] = available_quantity
    if allow_out_of_stock_purchases is not None:
        payload["allowOutOfStockPurchases"] = allow_out_of_stock_purchases

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status == 200:
                return await response.json()
            else:
                response.raise_for_status()