from tkinter import *
from tkinter import ttk
import psutil

root = Tk();

# Window
root.title("Pynalysis");
root.minsize(500, 300)


# Frame
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

#Create a canvas object
canvas= Canvas(win, width= 1000, height= 750, bg="SpringGreen2")

#Add a text in Canvas
canvas.create_text(300, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))
canvas.pack()

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# Testing the psutil library for both CPU and RAM performance details
print(psutil.cpu_percent())
print(psutil.virtual_memory().percent)


processes = [psutil.Process(pid=p.info['pid']) for p in psutil.process_iter(['pid', 'name'])]

# Sort the processes by memory usage
processes = sorted(processes, key=lambda p: p.memory_info().rss, reverse=True)

# Print the memory usage and process name
for i in range(5):
    print("Process name:", processes[i].name())
    print("Memory usage:", processes[i].memory_info().rss / 1024 / 1024, "MB")

root.mainloop()