from tkinter import *
from tkinter.font import Font

window = Tk()
window.geometry('600x500')

main_label = Label(window, text="Basic Calculator",
                   font=Font(size=18), fg='red')
main_label.pack()

label_1 = Label(window, text="Enter first number",
                font=Font(size=16), fg='red')
label_1.place(x=20, y=50)

entry_1 = Entry(window, font=Font(size=16), fg='red')
entry_1.place(x=300, y=50)

label_2 = Label(window, text="Enter second number",
                font=Font(size=16), fg='red')
label_2.place(x=20, y=150)

entry_2 = Entry(window, font=Font(size=16), fg='red')
entry_2.place(x=300, y=150)

label_3 = Label(window, text="Result",
                font=Font(size=16), fg='red')
label_3.place(x=20, y=250)

entry_3 = Entry(window, font=Font(size=16), fg='red')
entry_3.place(x=300, y=250)

def getInput():
    num_1 = entry_1.get()
    num_2 = entry_2.get()
    return num_1, num_2

def calc(event):
    num_1, num_2 = getInput()
    opr = event.widget.cget('text')
    expression = num_1 + opr + num_2
    result = eval(expression)
    showOutput(result)

def showOutput(result):
    entry_3.delete(0, len(entry_3.get()))
    entry_3.insert(0, str(result))

operators = ['+', '-', '/', '*']
for i in range(4):
    btn = Button(window, text=operators[i], font=Font(size=16),
                   bg='red', fg='white', padx=10, pady=10, width=5)
    btn.place(x=20+(i*150), y=400)
    # event binding
    btn.bind('<Button-1>', calc)

window.mainloop()