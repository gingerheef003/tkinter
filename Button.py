from tkinter import *

top = Tk()
top.geometry("200x100")


b = Button(
    top,
    activebackground="red",
    activeforeground="black",
    bg="white",
    fg="red",
    command=lambda: print('Hello World!'),
    #font="",
    state="active",
    text="print 'Hello World!'",
)
b.pack()

top.mainloop()