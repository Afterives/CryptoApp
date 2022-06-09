from calendar import month
import datetime
from sqlite3 import Timestamp
from urllib import response
from matplotlib.markers import MarkerStyle
from requests import request
import requests
import pandas as pd
import matplotlib as plt

def dostepne_crypto():
        url = f'https://api.coingecko.com/api/v3/coins' 
        response = requests.get(url)
        data = response.json()

        id_crypto = []

        for asset in data:
            id_crypto.append(asset['id'])

        return id_crypto

def pobierz_wykres(coin_id = 'bitcoin', vs_currency = 'eur', days = 'max', interval = 'daily'):
    ids_crypto = dostepne_crypto()
    if coin_id in ids_crypto:
        url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
        payload = {'vs_currency': vs_currency, 'days': days, 'interval': interval}
        response = requests.get(url, params = payload)
        data = response.json()

        timestamp_list, price_list = [], []

        for price in data['prices']:
            timestamp_list.append(datetime.datetime.fromtimestamp(price[0]/1000))
            price_list.append(price[1])

        raw_data = {'timestamp': timestamp_list, 'price': price_list}
        df = pd.DataFrame(raw_data)
        return df

market_info_btc = pobierz_wykres('bitcoin', 'pln', days = "365")
market_info_usdt = pobierz_wykres('tether', 'pln', days = "365")
market_info_luna = pobierz_wykres('terra-luna', days = "365")
market_info_doge = pobierz_wykres('dogecoin', days = "365")
market_info_bcc = pobierz_wykres('bitcoin-cash', days = "365")
market_info_eth = pobierz_wykres('ethereum', days = "365")

print(market_info_btc['timestamp'])
