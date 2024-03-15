from tkinter import *

root=Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

newline = canvas.create_line(0, 0, 50, 100)
otherline = canvas.create_oval(50, 50, 100, 100, fill="blue")

root.mainloop()
