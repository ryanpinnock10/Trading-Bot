from django.shortcuts import render
from .keys import *
import requests, json
from rest_framework.decorators import api_view


# Create your views here.
def index(request):
    BASE_URL = 'https://paper-api.alpaca.markets'
    ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
    HEADERS = {"APCA-API-KEY-ID" : API_KEY, "APCA-API-SECRET-KEY" : SECRET_KEY}
    POSITIONS_URL = '{}/v2/positions'.format(BASE_URL)
    WATCHLIST_URL = '{}/v2/watchlists'.format(BASE_URL)

#get positions
    r = requests.get(POSITIONS_URL, headers=HEADERS)
    data = json.loads(r.content)
    positions_data = []

    for index in range(len(data)):
            position = {
                'symbol' : data[index]['symbol'],
                'qty' : data[index]['qty'],
                'bought_price' : data[index]['avg_entry_price'],
                'current_price' : data[index]['current_price'],
                'change_today' : data[index]['change_today']
            }

            positions_data.append(position)
#-------------------------------------------------------------------------
#get account
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    info = json.loads(r.content)

    account_data = []
    account = {
        'account_number' : info['account_number'],
        'buying_power' : info['buying_power'],
        'equity' : info['equity'],
    }
    account_data.append(account)
#-------------------------------------------------------------------------
#get watchlist, than get wacthlist assets from watchinglist ID
    r = requests.get(WATCHLIST_URL, headers=HEADERS)
    data = json.loads(r.content)
    watchlist_data = []
    asset_data = []

    for index in range(len(data)):
        watchlist = {
            'id' : data[0]['id'],
            'name' : data[0]['name']
        }
    watchlist_data.append(watchlist)
 
    ADD_ASSET_URL = '{}/v2/watchlists/{}'.format(BASE_URL, watchlist['id'])
    r = requests.get(ADD_ASSET_URL, headers=HEADERS)
    data = json.loads(r.content)
    asset_list = data['assets']
    print(data)

    for index in range(len(asset_list)):
        asset = {
            'symbol' : asset_list[index]['symbol']
        }

        asset_data.append(asset)
#-------------------------------------------------------------------------
#context rendered to html
    context = {
        'account_data' : account_data,
        'positions_data' : positions_data,
        'watchlist_data' : watchlist_data,
        'asset_data' : asset_data
    }
    return render(request, 'alpaca/account.htm', context)