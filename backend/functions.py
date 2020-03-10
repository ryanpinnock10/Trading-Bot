
import requests, json
from config import *


BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
POSITIONS_URL = '{}/v2/positions'.format(BASE_URL)
WATCHLIST_URL = '{}/v2/watchlists'.format(BASE_URL)
ADD_ASSET_URL = '{}/v2/watchlists:by_name'.format(BASE_URL)
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

def view_watchlists():
    r = requests.get(WATCHLIST_URL, headers=HEADERS)
    watch_list_info = json.loads(r.content)
    return watch_list_info

def add_watchlist(name, symbol):
    data = {
        "name":name, 
        "symbol":symbol
    }
    r = requests.post(WATCHLIST_URL, header=HEADERS)
    add_watchlist_info = json.loads(r.content)
    return add_watchlist_info

def watchlist_add(name, symbol):
    data = {
        "name":name, 
        "symbol":symbol
    }
    r = requests.post(ADD_ASSET_URL, headers=HEADERS)
    asset_info = json.loads(r.content)
    return asset_info

# response = watchlist_add("Test watchlist", 'IBM')
response = view_watchlists()
print(response)
# -------------------------------tests-----------------------------------------
# response1 = get_account()
# response2 = create_order("IBM", 10, "buy", "market", "gtc")
# response3 = get_orders()

# response = make_watchlist("Test watchlist", 'AMZN')
# print(response)

# print(response1)
# print(response2)
# print(response3)