from tkinter import *

top = Tk()
#top.attributes('-zoomed', True)
top.geometry("500x500")

b = Button(
    top,
    activebackground="black",
    activeforeground="green",
    bg="white",
    fg="red",
    command=lambda: print('Hello World!'),
    #font="",
    state="disabled",
    text="print",
)
b.place(relx=0.5, rely=0.5, anchor=CENTER)

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
st.place(relx=0.5, anchor=N)

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
    buttons[i].place(relx=i/6, y=30, relwidth=1/6)

top.mainloop()