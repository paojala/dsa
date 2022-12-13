from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.pyplot as plt


### MENUS ####
import tkinter as tk  
from tkinter import ttk  
from tkinter import Menu    

### MENUS END


# Calculates the recursive sum
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

def plot_other():
    fig = Figure(figsize=(5, 4), dpi=100)
    plt.scatter(xlist,ylist)
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.scatter(xlist,ylist)
    
    # A canvas must be manually attached to the figure (pyplot would automatically
    # do it).  This is done by instantiating the canvas with the figure as
    # argument.
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

# plot function is created for 
# plotting the graph in 
# tkinter window
def plot_recursive():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
  
    plt.scatter(xlist,ylist)
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.scatter(xlist,ylist)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
# the main Tkinter window
window = Tk()

#Exit action  
def _quit():  
   window.quit()  
   window.destroy()  
   exit()  

def _recursive():
    plot_recursive()

def _quick():
    print("Test")

def _bubble():
    pass

def _about():
    print("Test")


def _other():
    plot_other()

#Create Menu Bar  
menuBar=Menu(window)  
window.config(menu=menuBar)  
#File Menu  
fileMenu= Menu(menuBar, tearoff=0)  
fileMenu.add_command(label="bubblesort", command=_bubble)  
fileMenu.add_command(label="quicksort", command=_quick)
fileMenu.add_command(label="recursive", command=_recursive) 
fileMenu.add_command(label="other", command=_other) 

fileMenu.add_separator()  
fileMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="File", menu=fileMenu)  
#Help Menu  
helpMenu= Menu(menuBar, tearoff=0)  
helpMenu.add_command(label="About", command=_about)  
menuBar.add_cascade(label="Help", menu=helpMenu)

  
# setting the title 
window.title('Plotting in Tkinter')
  
# dimensions of the main window
window.geometry("500x500")
  
# button that displays the plot
plot_button = Button(master = window, 
                     command = plot_recursive,
                     height = 2, 
                     width = 10,
                     text = "Plot")
  
# place the button 
# in main window
plot_button.pack()
  
# run the gui
window.mainloop()