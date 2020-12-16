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
    state="disabled",
    text="print 'Hello World!'",
)
b.pack()

#funcion to enable or diable the button
def disen():
    if b['state'] == "normal":
        b['state'] = "disabled"
        st['text'] = "Enable"
    elif b['state'] == "disabled":
        b['state'] = "normal"
        st['text'] = "Disable"
    
st = Button(
    top,
    text="Enable",
    command=disen
)
st.pack()

#To show various reliefs
rlf1 = Button(
    top,
    text="Groove",
    relief=GROOVE
)
rlf1.pack(side=LEFT)

rlf2 = Button(
    top,
    text="Ridge",
    relief=RIDGE
)
rlf2.pack(side=LEFT)

rlf3 = Button(
    top,
    text="Sunken",
    relief=SUNKEN
)
rlf3.pack(side=LEFT)

rlf4 = Button(
    top,
    text="Flat",
    relief=FLAT
)
rlf4.pack(side=LEFT)

rlf5 = Button(
    top,
    text="Raised",
    relief=RAISED
)
rlf5.pack(side=LEFT)

rlf6 = Button(
    top,
    text="Solid",
    relief=SOLID
)
rlf6.pack(side=LEFT)

top.mainloop()