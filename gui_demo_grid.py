from tkinter import *

w = Tk()

b1 = Button(w,text="MyButton")
b1.grid(row=0,column=0)
b2 = Button(w,text="MyButton")
b2.grid(row=1,column=0)
b3 = Button(w,text="MyButton")
b3.grid(row=1,column=1)

w.mainloop()

