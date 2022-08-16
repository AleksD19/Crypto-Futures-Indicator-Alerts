from candleManager import returnCandles

from rsi import *
from bb import *
from adx import *

import traceback
from time import perf_counter

from threading import Thread
from threading import Lock
import sys



#List of List[indicator, timeframe, coin, value]
coinListOfList = []

def addItemToCoinList(indicator,timeframe,coin,indicatorValue):
    
    coinToAppend = indicator+"," + timeframe + "," + coin + "," + str(indicatorValue) + "\n"
    coinListOfList.append(coinToAppend)




def checkRsi(line,time):
    
    try:
        line = line.replace("\n","")
        
        highCandles,lowCandles,closeCandles = returnCandles(line,time)

        currentCandle = closeCandles[len(closeCandles)-1]
        rsi = returnRsi(closeCandles)
        adx = returnAdx(highCandles,lowCandles,closeCandles)
        upperBB,lowerBB = returnBB(closeCandles)

        if validateRsi(rsi):
            addItemToCoinList("rsi",time,line,rsi)

        if verifyAdx(adx):
            addItemToCoinList("adx",time,line,adx)

        if valdiateUpperBB(float(currentCandle),upperBB):
            addItemToCoinList("bbuppper",time,line,upperBB)

        if valdiateLowerBB(float(currentCandle),lowerBB):
            addItemToCoinList("bblower",time,line,lowerBB)        

            
    except Exception as e:
        print(f"Coin: {line}: Error: {e}")
        # if "list index out of range" not in str(e):
        #     print(e)


file1 = open('futuresCoins.txt', 'r')
Lines = file1.readlines()
file1.close()


symbols = int(sys.argv[1])
machine_count = int(sys.argv[2])
machine = int(sys.argv[3])
time = str(sys.argv[4])

per_machine = symbols // machine_count
start_range = per_machine * (machine - 1)
end_range = per_machine * machine

print(f"Machine: {machine} Started at: {start_range} Ends at: {end_range}")

start_time = perf_counter()

for line in Lines[start_range:end_range]:
    checkRsi(line,time)

end_time = perf_counter()
print(f"It took {end_time - start_time:0.2f} seconds to complete data aquiring.")

with open(f"Machine{machine}.csv", "w") as file:
    for coin in coinListOfList:
        file.write(coin)




# with open(f"Machine{machine}.txt", "w") as file:
#     for coin in goodCoins:
#         file.write(coin + "\n")

# for line in loop_lines:
#     try:
#         line = line.replace("\n","")
#         line = line.replace(" ","")
#         line = line.replace("/","")
#         highCandles,lowCandles,closeCandles = returnCandles(line,"1min")
        
#         rsi = returnRsi(closeCandles)

#         print(line + "rsi: " + str(rsi))
#     except Exception:
#         print(traceback.format_exc())


# def new_thread():
#     t = Thread(target=checkRsi, args=())
#     t.start()
#     threads_arr.append(t)

# threads_arr = []
# threads = 50

# for x in range(threads):
#     new_thread()
    
# for t in threads_arr:
#     t.join()
