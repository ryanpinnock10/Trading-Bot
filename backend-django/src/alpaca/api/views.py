from django.shortcuts import render
import requests, json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from ..keys import API_KEY, SECRET_KEY
from ..models import Positions
from .serializers import PositionSerializer


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

class create_order(CreateAPIView):
    queryset = Positions.objects.all()
    serializer_class = PositionSerializer



