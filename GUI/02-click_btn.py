from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry('400x500')

label = Label(window, text="Hello World", font=font.Font(size=16))
label.place(x=10, y=20)

def changeText():
    # print("Clicked on Button")
    label.configure(text='Hello Ravi')

btn = Button(window, text="Click Here", font=font.Font(size=16),
             command=changeText)
btn.place(x=10, y=450)

window.mainloop()