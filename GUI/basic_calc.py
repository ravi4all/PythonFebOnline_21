from tkinter import *
from tkinter.font import  Font

window = Tk()
window.geometry('600x500')

main_label = Label(window, text="Basic Calculator",
                   font = Font(size=18), fg='red')
main_label.pack()

label_1 = Label(window, text="Enter first number",
                font = Font(size=16), fg='red')
label_1.place(x = 20, y = 50)

entry_1 = Entry(window, font = Font(size=16), fg='red')
entry_1.place(x=300, y=50)

label_2 = Label(window, text="Enter second number",
                font = Font(size=16), fg='red')
label_2.place(x = 20, y = 150)

entry_2 = Entry(window, font = Font(size=16), fg='red')
entry_2.place(x=300, y=150)

label_3 = Label(window, text="Result",
                font = Font(size=16), fg='red')
label_3.place(x = 20, y = 250)

entry_3 = Entry(window, font = Font(size=16), fg='red')
entry_3.place(x=300, y=250)

def clear():
    entry_3.delete(0, len(entry_3.get()))

def add():
    clear()
    num_1 = entry_1.get()
    num_2 = entry_2.get()
    result = int(num_1) + int(num_2)
    entry_3.insert(0, str(result))
    print("Addition is",result)

def sub():
    clear()
    num_1 = entry_1.get()
    num_2 = entry_2.get()
    result = int(num_1) - int(num_2)
    entry_3.insert(0, str(result))
    print("Addition is",result)

def div():
    clear()
    num_1 = entry_1.get()
    num_2 = entry_2.get()
    result = int(num_1) / int(num_2)
    entry_3.insert(0, str(result))
    print("Addition is",result)

def mul():
    clear()
    num_1 = entry_1.get()
    num_2 = entry_2.get()
    result = int(num_1) * int(num_2)
    entry_3.insert(0, str(result))
    print("Addition is",result)

btn_1 = Button(window, text='+', font=Font(size=16),
               bg='red', fg='white', padx=10, pady=10, width=5,
               command=add)
btn_1.place(x=20, y=400)

btn_2 = Button(window, text='-', font=Font(size=16),
               bg='red', fg='white', padx=10, pady=10, width=5,
               command=sub)
btn_2.place(x=150, y=400)

btn_3 = Button(window, text='/', font=Font(size=16),
               bg='red', fg='white', padx=10, pady=10, width=5,
               command=div)
btn_3.place(x=280, y=400)

btn_4 = Button(window, text='*', font=Font(size=16),
               bg='red', fg='white', padx=10, pady=10, width=5,
               command=mul)
btn_4.place(x=410, y=400)

window.mainloop()