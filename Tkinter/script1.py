from tkinter import *

window=Tk()

btn=Button(window, text='Execute')
btn.grid(row=0, column=0)

e1=Entry(window)
e1.grid(row=0,column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=0,column=2)

window.mainloop()
