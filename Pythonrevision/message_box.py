from tkinter import *
import tkinter.messagebox

root=Tk()
tkinter.messagebox.showinfo("Tiitle", "Hi! Welcome")

response=tkinter.messagebox.askquestion("Question 1", "Do you like coffee")

if response=="yes":
    print("Here is a coffee for you")
else:
    response=tkinter.messagebox.askquestion("Question 2", "Do you like Tea")
    if response=="yes":
        print("Here is a Tea for you")

root.mainloop()
