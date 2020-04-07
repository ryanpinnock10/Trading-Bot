from django.shortcuts import render
import requests, json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from ..keys import API_KEY, SECRET_KEY


@api_view()
def get_account(request):
    BASE_URL = 'https://paper-api.alpaca.markets'
    ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
    HEADERS = {"APCA-API-KEY-ID" : API_KEY, "APCA-API-SECRET-KEY" : SECRET_KEY}

    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    data = json.loads(r.content)
    return Response(data)
    
@api_view(['GET', 'POST'])
def get_positions(request):
    BASE_URL = 'https://paper-api.alpaca.markets'
    HEADERS = {"APCA-API-KEY-ID" : API_KEY, "APCA-API-SECRET-KEY" : SECRET_KEY}
    POSITIONS_URL = '{}/v2/positions'.format(BASE_URL)

    r = requests.get(POSITIONS_URL, headers=HEADERS)
    data = json.loads(r.content)
    return Response(data)

@api_view()
def order_history(request):
    BASE_URL = 'https://paper-api.alpaca.markets'
    HEADERS = {"APCA-API-KEY-ID" : API_KEY, "APCA-API-SECRET-KEY" : SECRET_KEY}
    HISTORY_URL = '{}/v2/account/activities'.format(BASE_URL)

    r = requests.get(HISTORY_URL,  headers=HEADERS)
    data = json.loads(r.content)
    return Response(data)

@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        data = request.data
        print(data['symbol'])
        return Response({"message": "Got an order", "data": request.data})
        



