# Caleb Mouritsen
# 10/25/18
# Clock Program

from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import calendar
import datetime


def current_time():
    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes = minutes % 60
    hours = minutes // 60
    current_hour = hours % 24
    if current_hour >= 12:
        tag="PM"
    else:
        tag = "AM"
    # set the time zone
    current_hour = current_hour - 6
    # format the output
    timex = str(current_hour)+"."+str(current_minutes)+"."+str(current_seconds)+tag
    # return the output
   
    return timex

def quit(*args):
    root.destroy()

def show_time():
    time = current_time()
    # Show the time
    txt.set(time)
    #Trigger the tick after 1000ms
    root.after(1000, show_time)

# Use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", False)
root.configure(background='Purple')
root.bind("x", quit)
root.after(1000, show_time)

fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="yellow", background="purple")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
