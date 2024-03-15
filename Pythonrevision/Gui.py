# from tkinter import *
#
# window = Tk()
# label1 = Label(window, text="Hello World")
# label1.pack()
# window.mainloop()
#
# import tkinter
# root=tkinter.Tk()
# label= Label(root, text="Mallika")
# label.pack()
# root.mainloop()





# from tkinter import *
# root=Tk()
# newframe=Frame(root)
# newframe.pack()
#
# secondframe=Frame(root)
# secondframe.pack(side=BOTTOM)
# button1=Button(newframe, text="Click Here",  fg="Red")
# button2=Button(secondframe, text="Click Here", fg="Blue")
#
# button1.pack()
# button2.pack()
#
# root.mainloop()
















#
#
# from tkinter import *
# root=Tk()
# label1=Label(root,text="Firstname")
# label2=Label(root,text="Lastname")
#
# entry1=Entry(root)
# entry2=Entry(root)
#
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)
#
# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
#
# root.mainloop()












#
# from tkinter import *
# root=Tk()
# label1 = Label(root, text="Python", bg="Grey", fg="blue")
# label1.pack(fill=X)
#
# label2 = Label(root, text="Content", bg="pink", fg="black")
# label2.pack(side=LEFT, fill=Y)
#
# root.mainloop()














# from tkinter import *
#
# root=Tk()
#
# def function():
#     print("Welcome")
#
# button=Button(root,text="Click Here", command=function, fg="black", bg="pink")
# button.pack()
#
# root.mainloop()





from tkinter import *
class Tkinter:
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.pack()

        self.print_button = Button(self.frame, text="Click here", command=self.print_message)
        self.print_button.pack()

        self.quit_button = Button(self.frame, text="Exit", command=self.frame.quit)
        self.quit_button.pack(side=LEFT)

    def print_message(self):
        print("Button Clicked")

object = Tk()
b = Tkinter(object)
object.mainloop()






