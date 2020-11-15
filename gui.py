from tkinter import *
from counting_polyominos import counting_poly

root = Tk()

e = Entry(root, width=50)
e.pack()


def click():
    num = e.get()
    fixed_num = counting_poly({(0, 0)}, set(), [], int(num)) - counting_poly({(0, 0)}, set(), [], int(num)-1)
    label1 = Label(root, text="fixed("+str(num)+") = " + str(fixed_num))
    label1.pack()


myButton = Button(root, text="calculate fixed polyominos", padx=50, command=click)
myButton.pack()


root.mainloop()
