from tkinter import *
from threading import Thread
import time
from tkinter import ttk
import tkinter as tk
import psutil
#from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt
import datetime

## APP CONFIG
root = tk.Tk()
label = tk.Label(root, text="placeholder")
# Window
root.title("HealthPyProcess");
root.minsize(400, 600)
# Frame
frm = ttk.Frame(root, padding=100)
frm.grid()

label = tk.Label(frm, text="placeholder")

def stats():
    info = "CPU: " + str(psutil.cpu_percent()) + "%\n" \
    + "MEM: " + str(psutil.virtual_memory().percent) + "%"
    label['text'] = info
    label.grid(column=0, row=0)
    root.after(750, stats)


def app():
    
    processes = [psutil.Process(pid=p.info['pid']) for p in psutil.process_iter(['pid', 'name'])]
    # for p in psutil.process_iter(['pid', 'name']):
    #     print(psutil.Process(pid=p.info['pid']))

    # Sort the processes by memory usage
    processes = sorted(processes, key=lambda p: p.memory_info().rss, reverse=True)

    # Print the memory usage and process name
    result = ""
    for i in range(5):
        result += "Process name:"+ str(processes[i].name()) + "\n"
        result += "Memory usage:"+ str(processes[i].memory_info().rss / 1024 / 1024) + "MB" + "\n\n"
    ttk.Label(frm, text=result).grid(column=0, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)

if __name__== '__main__':
    stats()
    app()
    root.mainloop()

