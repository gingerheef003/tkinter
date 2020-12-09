import tkinter as tk

window = tk.Tk()

greet = tk.Label(
    text="Hello, World!!",
    fg="red",
    bg="yellow",
    width=10,
    height=10,
)
greet.pack()

button = tk.Button(
    text="Click ME",
    width=25,
    height=5,
    bg="blue",
    fg="black",
)
button.pack()

entry = tk.Entry(
    fg="pink",
    bg="black",
    width=50,
)
entry.pack()

name = entry.get()
print(name)

window.mainloop()

