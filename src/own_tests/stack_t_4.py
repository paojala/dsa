import tkinter as tk  
from tkinter import ttk  
from tkinter import Menu    
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.pyplot as plt

class Stack:
    def __init__(self):
        self.stack = []

    def check_empty(self, stack):
        return len(self.stack) == 0

    # Adding items into the stack
    def push(self, item):
        self.stack.append(item)
    
    # Removing an element from the stack
    def pop(self):
        if (self.check_empty(self.stack)):
            return None
        return self.stack.pop()
    
    def __str__(self):
        return (str(self.stack))
    
    def show_content(self):
        return self.stack

    def size(self):
        return len(self.stack)


stack1 = Stack()
stack1.push(55)
stack1.push(66)

print(stack1)

def draw_canvas():
    canvas.delete("all")
    canvas.create_text(200, 50, text=stack1, fill="black", font=('Helvetica 15 bold'))
    canvas.create_window(200, 140, window=entry1)
    canvas.pack()

window = tk.Tk()
canvas = tk.Canvas(window, width= 500, height= 500, bg="SpringGreen2")
entry1 = tk.Entry(window) 
draw_canvas()


#Exit action  
def _quit():  
   window.quit()  
   window.destroy()  
   exit()  

def _insert():
    x1 = int(entry1.get())
    stack1.push(x1)
    draw_canvas()

def _remove():
    popped = stack1.pop()
    draw_canvas()
    canvas.create_text(200, 200, text="Popped: "+str(popped), fill="black", font=('Helvetica 15 bold'))

def _show_content():
    draw_canvas()
    canvas.create_text(200, 200, text="Content: "+str(stack1), fill="black", font=('Helvetica 15 bold'))

def _show_size():
    draw_canvas()
    canvas.create_text(200, 200, text="Size: "+str(stack1.size()), fill="black", font=('Helvetica 15 bold'))

#Create Menu Bar  
menuBar=Menu(window)  
window.config(menu=menuBar)  
#File Menu  
fileMenu= Menu(menuBar, tearoff=0)  
fileMenu.add_command(label="insert", command=_insert)  
fileMenu.add_command(label="remove", command=_remove)
fileMenu.add_command(label="show_content", command=_show_content) 
fileMenu.add_command(label="show_size", command=_show_size) 

fileMenu.add_separator()  
fileMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="File", menu=fileMenu)  
#Help Menu  
helpMenu= Menu(menuBar, tearoff=0)  
menuBar.add_cascade(label="Help", menu=helpMenu)

  
# setting the title 
window.title('Plotting in Tkinter')
  
# dimensions of the main window
window.geometry("500x500")
    
# run the gui
window.mainloop()