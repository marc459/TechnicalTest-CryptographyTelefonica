from tkinter import *
import signal
from threading import Thread
import time
from tkinter import ttk
import tkinter as tk
import psutil
#from PIL import ImageTk,Image
import numpy as np
import datetime

## APP CONFIG
root = tk.Tk()
label = tk.Label(root, text="placeholder")
# Window
root.title("HealthPy Process🌱");
root.minsize(400, 600)
# Frame
frm = ttk.Frame(root, padding=100)
frm.grid()

label = tk.Label(frm, text="placeholder")
def handler(signum, frame):
    root.destroy
    exit()
def stats():

    info = "[ CPU and RAM usage ]\n\n" \
    + "CPU: " + str(psutil.cpu_percent()) + "%\n" \
    + "MEM: " + str(psutil.virtual_memory().percent) + "%\n"
    label['text'] = info
    label.grid(column=0, row=0)
    root.after(750, stats)

def scan(processes):
    print(processes[0].open_files())
def app():
    
    processes = [psutil.Process(pid=p.info['pid']) for p in psutil.process_iter(['pid', 'name'])]


    # Sort the processes by memory usage
    processes = sorted(processes, key=lambda p: p.memory_info().rss, reverse=True)

    # Print the memory usage and process name
    result = "  [ Most Abusing Process ]\n\n"
    for i in range(5):
        result += "Process name: "+ str(processes[i].name())  + "\n"
        result += "Memory usage: "+ str(round(processes[i].memory_info().rss / 1024 / 1024,2)) + " MB" + "\n\n"
        
    ttk.Label(frm, text=result).grid(column=0, row=1)
    ttk.Button(frm, text="Scan",command=lambda: scan(processes)).grid(column=0, row=2)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)
    
    root.after(2000, app)
    

if __name__== '__main__':
    signal.signal(signal.SIGINT, handler)
    try:
        stats()
        app()
        #scan()
    except:
        print("An exception occurred")
        root.destroy
        exit()
    root.mainloop()

