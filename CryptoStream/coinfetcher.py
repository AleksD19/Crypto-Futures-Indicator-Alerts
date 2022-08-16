from binance.client import Client
import numpy as np
import time
import talib
import traceback

api_key = "YOUR_API"
secret_key = "YOUR_SECRET"

client = Client(api_key, secret_key)


futures_exchange_info = client.futures_exchange_info()  # request info on all futures symbols
trading_pairs = [info['symbol'] for info in futures_exchange_info['symbols']]


with open("futuresCoins.txt", "w") as file:
    for coin in trading_pairs:
        file.write(coin + "\n")