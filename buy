import websocket
import json
from binance.exceptions import BinanceAPIException
from binance.client import Client
import requests
import datetime
import os
from dotenv import load_dotenv
from pathlib import Path
amount = 0.01
repeat = 'Once'
initial = 1


class TradeBot:
    def __init__(self):
        self.SYMBOL = 'BTCUSDT'
        
        self.SITE_URL = 'http://64.226.103.148:8002'
        self.amount = 0.0033
        self.token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImJveEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImJveCIsImV4cCI6MTY4Mzk1NjU2Mn0.3SDwJ6xp9LQjMqEFs5Qbdsa0R9ZlATt8gjT5TND9o3A'
        self.id = 1
        self.mode = 'buy'
        self.api_key = "QSOAqPicgAdGuxFrUX3fRyliUKwZvMZz5W2vmozNIZrxUu4hUw5FIRkv1G2TO4F2"
        self.secret_key = "vYvmMCee2XSKd5o4asykDoB8lR93XCSvAYYWRjA9Fk4tF0mOtEByijNEMX3TVyCl"
        self.socket = "wss://stream.binance.com:9443/ws/" + 'btcusdt' + "@kline_1m"
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        self.client = Client(self.API_KEY, self.SECRET_KEY, testnet=True)
        ws = websocket.WebSocketApp(self.socket, on_open=self.on_open, on_close=self.on_close,
                                    on_error=self.on_error, on_message=self.on_message)
        ws.run_forever()

    def on_open(self, ws):
        print("Connection Opened")

    def on_close(self, ws):
        print("Connection close")

    def on_error(self, ws, error):
        print("Here is an error:", error)

    def on_message(self, ws, message):
        try:
            self.my_order = self.client.create_order(symbol='BTCUSDT',
                                                     side=self.mode, type=self.client.ORDER_TYPE_MARKET,
                                                     quantity=self.amount)
            print(self.my_order)
            self.order = json.dumps(self.my_order)
            with open('tradehistory.json', 'a') as fl:
                fl.write(',')
                fl.write(self.order)
            price = self.my_order.get('fills')[-1].get('price')
            self.my_order.pop('fills')
            b = ['origQty', 'cummulativeQuoteQty', 'selfTradePreventionMode']
            for i in b:
                self.my_order.pop(i)
            self.my_order['price'] = price
            self.my_order['id'] = self.id
            self.my_order['executedQty'] = self.amount
            self.my_order['flag']='True'
            data = requests.post(url=self.SITE_URL + '/user_exchanges/bin', data=self.my_order,
                                 headers={'Authorization': self.token})
            data = data.json()
            print(data)
            logs={'id':self.id,'symbol':self.SYMBOL,
                  'price':price,
                  'quantity':self.amount,'side':self.mode,'exchange':'Binance'}
            data=requests.post(url=self.SITE_URL+'/user_exchanges/logs',data=logs,
                               headers={'Authorization':self.token})

            data = data.json()
            print(data)
            ws.close()
        except BinanceAPIException as e:
            print(e)
            data = {'message': 'Failed', 'data': 'Not Enough balance'}
            print(data)
            data = json.dumps(data)
            with open('tradehistory.json', 'a') as fl:
                fl.write(',')
                fl.write(data)
            data = {'id': self.id, 'status': False, 'message': 'Balance not found', 'side': self.mode,
                    'symbol': self.SYMBOL,
                    'quantity': self.amount, 'time': str(datetime.datetime.now()), 'Exchange_name': 'Binance'}
            data = requests.post(url=self.SITE_URL + '/user_exchanges/bin', data=data,
                                 headers={'Authorization': self.token})
            data = data.json()
            print(data)
            ws.close()
            # return e
TradeBot()
        
