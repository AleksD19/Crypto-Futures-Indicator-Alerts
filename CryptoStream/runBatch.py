import os
import tkinter as tk
from tkinter import *
from threading import Thread
import csv
import winsound
from datetime import datetime 

machines = 15
symbols = 155
times = ["5min","15min"]
threads = []





def newThread(x,time):
    os.system(f'cmd /c "python stream.py {symbols} {machines} {x} {time}"')

def showData():
#indicator,timeframe,coin,val
    for i in range(1,machines+1):
        
        with open(f"Machine{i}.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                rsiSize = rsiListbox.size()
                adxSize = adxListbox.size()
                bbSize= bbListbox.size()

                rounded = round(float(row[3]),2)
                
                if row[0] == "rsi":
                    
                    if float(row[3]) < 20:
                        rsiListbox.insert("end",str(row[2]) + " " + str(rounded) + " (" + row[1] + ")" )
                        rsiListbox.itemconfig(rsiSize, {'bg':'green'})
                    elif float(row[3]) > 80:   
                        rsiListbox.insert("end",str(row[2]) + " " + str(rounded) + " (" + row[1] + ")")
                        rsiListbox.itemconfig(rsiSize, {'bg':'red'})
                        
                elif row[0] == "adx":
                    
                    if float(row[3]) < 15:                   
                        adxListbox.insert("end", str(row[2]) + " " + str(rounded) + " (" + row[1] + ")")                        
                        adxListbox.itemconfig(adxSize, {'bg':'cyan'})
                    elif float(row[3]) > 55:                        
                        adxListbox.insert("end",str(row[2]) + " " + str(rounded) + " (" + row[1] + ")")                                                             
                        adxListbox.itemconfig(adxSize, {'bg':'cyan'})               
                elif row[0] == "bbupper":
                    bbListbox.insert("end",row[2] + " (" + row[1] + ")")
                    bbListbox.itemconfig(bbSize, {'bg':'red'})
                elif row[0] == "bblower":
                    bbListbox.insert("end",row[2] + " (" + row[1] + ")")
                    bbListbox.itemconfig(bbSize, {'bg':'green'})

 

root = Tk()
root.title("Binance Futures Indicator Signals")
rsiLabel= tk.Label(root, text="RSI")
rsiLabel.configure(font=("Times New Roman", 15, "bold"))
rsiLabel.grid(row=0,column=0)

bbLabel= tk.Label(root, text="BB")
bbLabel.configure(font=("Times New Roman", 15, "bold"))
bbLabel.grid(row=0,column=1)

adxLabel= tk.Label(root, text="ADX")
adxLabel.configure(font=("Times New Roman", 15, "bold"))
adxLabel.grid(row=0,column=2,sticky="ns")

combinedLabel= tk.Label(root, text="Combined")
combinedLabel.configure(font=("Times New Roman", 15, "bold"))
combinedLabel.grid(row=0,column=3,sticky="ns")

root.grid_rowconfigure(1, weight=2)


rsiListbox = Listbox(root)
rsiListbox.grid(row=1,column=0,sticky="nsew")

bbListbox = Listbox(root)
bbListbox.grid(row=1,column=1,sticky="nsew")

adxListbox = Listbox(root)
adxListbox.grid(row=1,column=2,sticky="nsew")


combinedListbox = Listbox(root)
combinedListbox.grid(row=1,column=3,sticky="nsew")


def clearListBoxes():
    rsiListbox.delete(0,END)
    bbListbox.delete(0,END)
    adxListbox.delete(0,END)

def update():

    print("Checking..")
    currentTime  = datetime.now()

    calculated = False

    cleared = False

    for myTime in times:
        
        trimmedTime = myTime.replace("min","")
        parsedTime = int(trimmedTime)

        if(currentTime.minute % parsedTime) ==0 :
            if cleared == False:
                clearListBoxes()
                cleared = True
                
            calculated =True
            for x in range(machines):
                t = Thread(target=newThread, args=(x + 1,myTime))
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

            showData()

            if(rsiListbox.size() > 0):
                freq = 1500
                dur = 250

                winsound.Beep(freq,dur)
                winsound.Beep(freq,dur)

                

    if calculated == False:
        root.after(1000, update)
    else:
        root.after(60000, update)
    return
 
try:
    root.after(3000, update)
except:
    pass

root.mainloop()


















                                    