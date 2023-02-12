from tkinter import *
import signal
from threading import Thread
import datetime
from tkinter import ttk
import tkinter as tk
import psutil
import numpy as np
import re

import os

## APP CONFIG
root = tk.Tk()
label = tk.Label(root, text="placeholder")
# Window
root.title("HealthPy Process🌱");
root.minsize(400, 600)
# Frame
frm = ttk.Frame(root, padding=50)
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

class Process:
    def __init__(self, name,has_internet, suspiciouspaths):
        self.name = name
        self.has_internet = has_internet
        self.suspiciouspaths = suspiciouspaths
    def add_element(self, element):
        self.suspiciouspaths.append(element)
    def get_name(self):
        return self.name
    def get_suspiciouspaths(self):
        return self.suspiciouspaths
    def get_has_internet(self):
        return self.has_internet

def fullScan(processes):
    canvastxt=""
    processArray=[]
    ret=""
    for i in range(len(processes)):
        try:
            paths=re.findall(r"path='[^']*'",str(processes[i].open_files()))
        except:
            pass
        try:
            print(processes[i].connections())
            if processes[i].connections().index('ESTABLISHED'):
                processArray.append(Process(processes[i].name(),True, []))
        except:
            processArray.append(Process(processes[i].name(),False, []))
        
        for path in paths:
            if(path.find("/tmp") > 0 or path.find("/dev/shm") > 0 or path.find("/.") > 0):
                canvastxt+= path +"\n"
                processArray[i].add_element(path)
    if(canvastxt ==""):
        canvas("All process directories must appear legitime correct!")
    else:
        for i in range(5 if len(processArray) > 5 else len(processArray)):
            ret += "Name: " + processArray[i].get_name() + " - Internet conexion: " + str(processArray[i].get_has_internet()) + "\n" 
            for x in range(len(processArray[i].get_suspiciouspaths())):
                if(x < 3):
                    ret += processArray[i].get_suspiciouspaths()[x] + "\n"
            ret+="\n"
        canvas("Some process appear to having access to suspicious directories:\n" + ret + "\n\n Full report is saved in " + str(datetime.datetime.now()) + ".log")

    if(ret != ""):
        try:
            if not os.path.exists("logs"):
                os.makedirs("logs")
            f = open("./logs/" + str(datetime.datetime.now()) + ".log", "a")
            f.write(ret)
            f.close()
        except:
            print("Could not print on Log File")
    
    
def app():
    
    processes = [psutil.Process(pid=p.info['pid']) for p in psutil.process_iter(['pid', 'name'])]


    # Sort the processes by memory usage
    processes = sorted(processes, key=lambda p: p.memory_info().rss, reverse=True)

    # Print the memory usage and process name
    result = ""
    
    i=0
    scanBtns=[]
    ttk.Label(frm, text="  [ Most Abusing Process ]\n\n").grid(column=0, row=i+1)
    while(i<5):
        result = "Name: "+ str(processes[i].name())  + "\n" \
        + "RAM:   "+ str(round(processes[i].memory_info().rss / 1024 / 1024,2)) + " MB" + "\n"
        ttk.Label(frm, text=result).grid(column=0, row=i+2)
        i+=1
    
    ttk.Button(frm, text="Fullscan", command=lambda: fullScan(processes)).grid(column=0, row=i+2)
    root.after(2000, app)

def canvas(output):
    canvas=tk.Canvas(root, width=1000, height=700, background='white', scrollregion=(0,0,500,500))
    canvas.grid(column=3,row=0)
    canvas.create_text(40, 30, text="Report", font=("TkDefaultFont", 9), fill="red")
    canvas.create_text(500, 350, text=output, font=("TkDefaultFont", 9))
    #root.after(2000, canvas)

if __name__== '__main__':
    signal.signal(signal.SIGINT, handler)
    try:
        stats()
        app()
        canvas("output")
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1000)
    except Exception as e:
        print("An exception occurred\n" + str(e))
        root.destroy
        exit()
    root.mainloop()

