import alpaca_trade_api as tradeapi
# from .config import *
API_KEY = "PKQBQNZ5UE5V81TGITGN"
SECRET_KEY = "ceSxlGQPKbjEF37i2uywLE7AqXWjRMd/a7Sc7fOZ"


conn = tradeapi.stream2.StreamConn()

api = tradeapi.REST(API_KEY, SECRET_KEY, api_version='v2')

# Handle updates on an order you've given a Client Order ID.
# The r indicates that we're listening for a regex pattern.
client_order_id = r'my_client_order_id'
@conn.on(client_order_id)
async def on_msg(conn, channel, data):
    # Print the update to the console.
    print("Update for {}. Event: {}.".format(client_order_id, data['event']))

# Start listening for updates.
conn.run(['trade_updates'])


