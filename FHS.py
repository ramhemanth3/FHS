#!/usr/bin/python
import random
import tkinter as tk
import os
from tkinter import * 
from tkinter.ttk import *

root = tk.Tk()
root.geometry("1920x1080")
def getPresFold():
    address = os.getcwd()
    w = tk.Label(root, text = address)
    w.pack()

getPresFold()
currAdd = Button(root, text = " Current Address ", compound = LEFT, command = getPresFold).pack( side = LEFT ) 

root.mainloop()