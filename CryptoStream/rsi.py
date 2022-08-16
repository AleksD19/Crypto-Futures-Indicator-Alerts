import numpy as np
import talib


topRsi = 85
bottomRsi = 15


def returnRsi(candleList):

    floatCandles = [float(x) for x in candleList]
    np_float_Candles = np.array(floatCandles)
    output = talib.RSI(np_float_Candles, timeperiod=14)

    return output[len(output) -1]


def validateRsi(rsi):
    if rsi>80:
        return True
    elif rsi < 20:
        return True
    return False

    


