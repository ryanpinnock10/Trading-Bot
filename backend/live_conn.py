import requests
import alpaca_trade_api as tradeapi
from config import *


conn = tradeapi.stream2.StreamConn()

api = tradeapi.REST(
    base_url=BASE_URL, 
    key_id=API_KEY, 
    secret_key=SECRET_KEY, 
    api_version='v2'
    )

account = api.get_account()

print(account)

# Handle updates on an order you've given a Client Order ID.
# The r indicates that we're listening for a regex pattern.
# client_order_id = r'my_client_order_id'
# @conn.on(client_order_id)
# async def on_msg(conn, channel, data):
#     # Print the update to the console.
#     print("Update for {}. Event: {}.".format(client_order_id, data['event']))

# # Start listening for updates.
# conn.run(['trade_updates'])


