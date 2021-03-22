from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry('400x500')

font = font.Font(size=16)

# label = Label(window, text="", font=font)
# label.place(x=10, y=20)

textbox = Entry(window, font=font)
textbox.place(x = 10, y = 400)

def changeText():
    # print("Clicked on Button")
    label = Label(window, text="", font=font)
    # label.place(x=10, y=20)
    label.pack()
    value = textbox.get()
    # label.configure(text=' '+username)
    label.configure(text=value)

btn = Button(window, text="Click Here", font=font,
             command=changeText)
btn.place(x=10, y=450)

window.mainloop()