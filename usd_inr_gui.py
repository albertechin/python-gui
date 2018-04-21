from tkinter import *

def usd_to_inr():
    inr = float(e1_val.get()) * 65.68
    t1.insert(END, inr)


window = Tk()

b1 = Button(window, text="Convert",command = usd_to_inr)
b1.grid(row=0, column=0)

e1_val = StringVar()

e1 = Entry(window,textvariable = e1_val)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width= 20)
t1.grid(row=0, column=2)

window.mainloop()
