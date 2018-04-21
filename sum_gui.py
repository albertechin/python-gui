from tkinter import *

def sum():
    n=int(e1_val.get())+int(e2_val.get())
    t1.insert(END,n)


w = Tk()


e1_val = StringVar()
e1 = Entry(w, textvariable=e1_val)
e1.grid(row=0, column=0)

e2_val = StringVar()
e2 = Entry(w, textvariable=e2_val)
e2.grid(row=0, column=1)

b1 = Button(w,text="Sum",command=sum)
b1.grid(row=2, column=0)

t1 = Text(w, height=1, width=20)

t1.grid(row=3, column=0)



w.mainloop()
