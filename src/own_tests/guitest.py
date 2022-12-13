#Create Menubar in Python GUI Application  
import tkinter as tk  
from tkinter import ttk  
from tkinter import Menu  
win = tk.Tk()  
win.title("Python GUI App")  
#Exit action  
def _quit():  
   win.quit()  
   win.destroy()  
   exit()  

def _quick():
    pass

def _bubble():
    pass

#Create Menu Bar  
menuBar=Menu(win)  
win.config(menu=menuBar)  
#File Menu  
fileMenu= Menu(menuBar, tearoff=0)  
fileMenu.add_command(label="bubblesort", command=_bubble())  
fileMenu.add_command(label="quicksort", command=_quick()) 

fileMenu.add_separator()  
fileMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="File", menu=fileMenu)  
#Help Menu  
helpMenu= Menu(menuBar, tearoff=0)  
helpMenu.add_command(label="About")  
menuBar.add_cascade(label="Help", menu=helpMenu)  

#Recursive

def recursive(n):
    if n == 0:
        return 1
    else:
        result = 1 / (1 + recursive(n - 1))
        return result

# Test
xlist = []
ylist = []
for n in range(0,10):
    xlist.append(n)
    ylist.append(recursive(n))

import numpy as np
import matplotlib.pyplot as plt

win.geometry("500x500")

plt.scatter(xlist,ylist)

plot_button = tk.Button(master = win,
                     height = 2,
                     width = 10,
                    text = "Plot")

fig = Figure(figsize = (5, 5),
                 dpi = 100)

plot_button.pack()

#Canvas

w = tk.Canvas(win, width=200, height=100)
w.pack()

w.create_rectangle(50, 20, 150, 80, fill="#476042")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0, 0, 50, 20, fill="#476042", width=3)
w.create_line(0, 100, 50, 80, fill="#476042", width=3)
w.create_line(150,20, 200, 0, fill="#476042", width=3)
w.create_line(150, 80, 200, 100, fill="#476042", width=3)



#Calling Main()  
win.mainloop()  