import tkinter as tk
from tkinter import ttk

#window
win = tk.Tk()
win.title("Python GUI")
win.geometry("500x300")

#text
title_lable =  ttk.Label(win, text="Enter km/h", font=("Arial", 16))    
title_lable.pack()

#input field
number_input = tk.Entry(win, width=10)
number_input.pack()

#button
number = 0
def convert():
    number = number_input.get()
    number = int(number)
    result_label = ttk.Label(win)
    result_label.config(text=str(number) + " km/h = " + str(number * 0.62137) + " miles/h")
    resutl_lable.pack()

button = tk.Button(win, text="Convert", command=convert)
button.pack()


#run
win.mainloop()