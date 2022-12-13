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

# plot function is created for 
# plotting the graph in 
# tkinter window
def plot():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
  
    plt.scatter(xlist,ylist)

    # list of squares
    y = [i**2 for i in range(101)]
  
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
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
  
# the main Tkinter window
window = Tk()

#Exit action  
def _quit():  
   window.quit()  
   window.destroy()  
   exit()  

def _recursive():
    plot()

def _quick():
    print("Test")

def _bubble():
    pass

def _about():
    print("Test")

#Create Menu Bar  
menuBar=Menu(window)  
window.config(menu=menuBar)  
#File Menu  
fileMenu= Menu(menuBar, tearoff=0)  
fileMenu.add_command(label="bubblesort", command=_bubble)  
fileMenu.add_command(label="quicksort", command=_quick)
fileMenu.add_command(label="recursive", command=_recursive) 

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
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Plot")
  
# place the button 
# in main window
plot_button.pack()
  
# run the gui
window.mainloop()