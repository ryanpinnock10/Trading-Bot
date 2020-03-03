import json
from firebase import firebase
from .functions import *

FIREBASE_URL = "https://trade-bot-a7ed8.firebaseio.com/"
firebase = firebase.FirebaseApplication(FIREBASE_URL, None)

def input_alpaca_data():    
    #don't run unless you're using a different Alpaca account. Will duplicate entry

    data = firebase.post('Alpaca_user', account_info)

def input_alpaca_orders():
    data = firebase.post('Orders', orders_info)


input_alpaca_orders()
