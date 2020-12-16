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

top.mainloop()