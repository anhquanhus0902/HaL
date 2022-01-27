from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk

window = Tk()
window.title("Test app")

# Set the window size
window.geometry("500x500")

# Create a label
lb1 = tk.Label(window, text="Hello Tkinter", fg="red", font=("Arial Bold", 10))
lb1.grid(column=0, row=0)

# Create a textbox
txtb = Entry(window, width=10)
txtb.grid(column=0, row=1)

def handleButton1():
    # lb1.configure(text="Yahooooo " + txtb.get())
    messagebox.showinfo("Message", "Hello " + txtb.get())
    return 

# Create a button
btn = Button(window, text="Click Me", command=handleButton1)
btn.grid(column=1, row=1)

# Create a combobox
cb = Combobox(window)
cb['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
cb.current(3)
cb.grid(column=0, row=2)

def handleButton2():
    lb1.configure(text="Yahooooo " + cb.get())
    return

btn2 = Button(window, text="Click Me2", command=handleButton2)
btn2.grid(column=1, row=2)

# Create a textarea
txta = Text(window, width=30, height=3, border=3)
txta.grid(column=0, row=3)

window.mainloop()