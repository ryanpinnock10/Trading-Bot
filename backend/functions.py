
import requests, json
from config import *


BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
POSITIONS_URL = '{}/v2/positions'.format(BASE_URL)
# ALL_ORDERS_URL = '{}/v2/orders:by_client_order_id'.format(BASE_URL)
HEADERS = {"APCA-API-KEY-ID" : API_KEY, "APCA-API-SECRET-KEY" : SECRET_KEY}

def get_account():
    global account_info
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    account_info = json.loads(r.content)
    return account_info

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol":symbol,
        "qty":qty,
        "side":side,
        "type":type,
        "time_in_force":time_in_force

    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    info = json.loads(r.content)
    return info
    
def get_orders():
    global orders_info
    r = requests.get(POSITIONS_URL, headers=HEADERS)
    orders_info = json.loads(r.content)
    return orders_info

# response = create_order("AMD", 50, "buy", "market", "gtc")
response2 = get_orders()

# print(response)
# print(response2)