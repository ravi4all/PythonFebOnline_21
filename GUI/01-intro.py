from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry('400x500')

label = Label(window, text="Hello World", font=font.Font(size=16))
# label.pack()
# label.grid(row=0,column=0)
label.place(x=10, y=20)

btn = Button(window, text="Click Here", font=font.Font(size=16))
# btn.pack()
# btn.grid(row=0,column=1)
btn.place(x=10, y=450)

window.mainloop()