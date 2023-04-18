import websocket
import json
from binance.exceptions import BinanceAPIException
from binance.client import Client
import pandas as pd

import requests
import datetime
amount = 0.0033
repeat = 'Once'
initial = 1
class TradeBot:
    def __init__(self):
        self.SYMBOL = 'BTCUSDT'
        self.amount = 0.0033
        self.mode='buy'
        self.socket = "wss://stream.binance.com:9443/ws/" + 'btcusdt' + "@kline_1m"
        self.API_KEY = 'gR0FLVP4exAt7Tf54gfWG3E6iPGvwSazf8UsaRocCtUyNY176BmLkDKuncq7XX5W'
        self.SECRET_KEY = 'OBItjPQ16JNcqT0QpqReQXWRZZVs6Bot8cUePDyigmLe3oT5GkicLah4kIWSbV5k'
        self.client = Client(self.API_KEY, self.SECRET_KEY, testnet=False)
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
            self.my_order = self.client.create_order(symbol=self.SYMBOL.upper(),
                                                     side=self.mode, type=self.client.ORDER_TYPE_MARKET,
                                                     quantity=0.0033)
            print(self.my_order)
            ws.close()
            
        except BinanceAPIException as e:
            print(e)
            ws.close()

TradeBot()


        
