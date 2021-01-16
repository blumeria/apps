"""
This mini-app reminds you to move every X minutes.
Simone Oberhaensli, 2021-01
"""

import tkinter as tk
from tkinter import *
import time

# create the main window
root= tk.Tk()
root.title(" Time tracking desktop app ")
root.geometry("300x150")

# create a frame for the buttons on the bottom of window
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
# and one for the input block
topframe = Frame(root)
topframe.pack( side = TOP)


# define the clock label
clock = Label(root, font=('times', 20, 'bold'))
clock.pack(fill=BOTH, expand=1)


# count number of minutes after start
def current_time():
    minutes = int(minvar.get())
    time = 1000*60*minutes
    clock.after(time, printstuff)
# the print message
def printstuff():
    clock.config(text = "Time to move!", font=("arial", 25))

# delete the message
def reset_time():
    clock.config(text = "")

# create two bottons, one to start the time counting
# one for reset
b1 = tk.Button(bottomframe, text ="start", command = current_time)
b2 = tk.Button(bottomframe, text = " reset", command = reset_time)
b1.pack(side = LEFT)
b2.pack(side = RIGHT)
# create an input block for the time interval
minvar = tk.StringVar()
e1 = Entry(topframe, textvariable = minvar)
e1.pack(side=BOTTOM)
Label(topframe, text="Please enter the time in minutes:",
      font=("arial", 12) ).pack(side = TOP)

root.mainloop()