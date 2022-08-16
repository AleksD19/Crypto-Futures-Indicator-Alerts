from binance.client import Client
import numpy as np
import talib


# ADX Value	Trend Strength
# 0-25	Absent or Weak Trend
# 25-50	Strong Trend
# 50-75	Very Strong Trend
# 75-100	Extremely Strong Trend


def returnAdx(high,low,close):

    highCandles = [float(x) for x in high]
    np_highCandles = np.array(highCandles)

    lowCandles = [float(x) for x in low]
    np_lowCandles = np.array(lowCandles)

    closeCandles = [float(x) for x in close]
    np_closeCandles = np.array(closeCandles)

    
    real = talib.ADX(np_highCandles, np_lowCandles, np_closeCandles, timeperiod=14)
    
    returnAdx= real[len(real)-1]
    

    return returnAdx

def verifyAdx(currentAdx):
    if currentAdx >60:
        return True
    elif currentAdx < 15:
        return True
    
    return False
