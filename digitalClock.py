# for GUI module kit
from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")

def get_time():
    # format display hour, minutes, seconds, am/pm
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    # every 0,2 seconds it will run function to get the most recent
    clock.after(200,get_time)

# set the style 
clock = Label(master, font=('Calibri', 90), bg='grey',fg='white' )
# put on center of the screen
clock.pack()

get_time()

master.mainloop()





