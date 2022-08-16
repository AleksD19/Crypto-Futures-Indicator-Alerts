from binance.client import Client
import numpy as np
import talib



def returnBB(candleList):
    floatCandles = [float(x) for x in candleList]
    np_float_Candles = np.array(floatCandles)
    upperband, middleband, lowerband = talib.BBANDS(np_float_Candles, timeperiod=20, nbdevup=2, nbdevdn=2)

    return upperband[len(upperband)-1],lowerband[len(lowerband)-1]

def valdiateUpperBB(currentCandle,upperBB):

    if currentCandle >=upperBB:
        return True
    return False

def valdiateLowerBB(currentCandle,lowerBB):

    if currentCandle <=lowerBB:
        return True
    return False