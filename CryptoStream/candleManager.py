from binance.client import Client
import numpy as np
import time
import talib
import traceback

api_key = "YOUR_KEY"
secret_key = "YOUR_SECRET"

client = Client(api_key, secret_key)

#Open time, Open, High, Low, Close, Volume, Close time, Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Ignore

def returnCandles(symbol, time):

    candleCloseVals = []
    candleHighVals = []
    candleLowVals = []

    allCandles =[]

    if time == "5min":
        allCandles = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_5MINUTE, "8 hours ago UTC")
    elif(time == "15min"):
        allCandles = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, "26 hours ago UTC")

    
    for c in allCandles:
        high = c[2]
        low = c[3]
        close = c[4]

        candleHighVals.append(high)
        candleLowVals.append(low)
        candleCloseVals.append(close)

     
    if len(candleCloseVals) != 0:
        candleCloseVals.pop(len(candleCloseVals) - 1)

    if len(candleHighVals) != 0:
        candleHighVals.pop(len(candleHighVals) - 1)

    if len(candleLowVals) != 0:
        candleLowVals.pop(len(candleLowVals) - 1)

        
    return candleHighVals,candleLowVals,candleCloseVals

    
