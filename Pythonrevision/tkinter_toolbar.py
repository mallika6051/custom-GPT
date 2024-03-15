from tkinter import *

def function():
    print("Button clicked")

root=Tk()

myMenu=Menu(root)
root.config(menu=myMenu)

subMenu=Menu(myMenu)
myMenu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="Project", command=function)
subMenu.add_command(label="Save", command=function)

subMenu.add_separator()
subMenu.add_command(label="Exit", command=function)

newMenu=Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=newMenu)
newMenu.add_command(label="Undo", command=function)

toolbar=Frame(root, bg="pink")
insertbutton=Button(toolbar, text="Insert Files", command=function)
insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton=Button(toolbar, text="print", command=function)
printbutton.pack(side=LEFT, padx=2, pady=3)
toolbar.pack(side=TOP, fill=X)

status=Label(root, text="This is status bar", bd=1, relief=FLAT, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
