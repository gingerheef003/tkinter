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
    text="print",
)
b.grid(row=0, column=0)

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
st.grid(row=0, column=1)

#To show various reliefs
buttons = []
reliefs = [
    "groove",
    "ridge",
    "sunken",
    "flat",
    "raised",
    "solid",
]
for i in range(6):
    buttons.append(Button(top, relief=reliefs[i], text=reliefs[i].title()))
    buttons[i].grid(row=1, column=i)

top.mainloop()