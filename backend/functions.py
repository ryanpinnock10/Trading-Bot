
import requests, json
from config import *


BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
HEADERS = {"APCA-API-KEY-ID" : API_KEY, "APCA-API-SECRET-KEY" : SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    info = json.loads(r.content)
    return info["account_number"], info["status"], info["cash"], info["equity"], info["last_equity"]

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol":symbol,
        "qty":qty,
        "side":side,
        "type":type,
        "time_in_force":time_in_force

    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)

response = get_account()

print(response)