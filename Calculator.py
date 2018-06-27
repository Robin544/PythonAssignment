#                               Calculator in Python

# Importing tkinter

import tkinter
from tkinter import *
master = tkinter.Tk()


# click the numbers and operators in the calculator

def click(numbers):
    global operator
    operator = operator + str(numbers)
    input1.set(operator)


# clears the screen

def clear():
    global operator
    operator = ""
    input1.set("0")


# shows the result

def equal():
    global operator
    result = str(eval(operator))
    input1.set(result)
    operator = ""


master.title("Calculator")
operator = ""

input1 = StringVar()

display = Entry(master, textvariable=input1, bd=20, insertwidth=2, justify="right").grid(columnspan=4)

bt15 = Button(master, bd=3, padx=16,  text="(", width=1, height=2, command=lambda: click("(")).grid(column=0, row=1)
bt16 = Button(master, bd=3, padx=16,  text=")", width=1, height=2, command=lambda: click(")")).grid(column=1, row=1)
bt17 = Button(master, bd=3, padx=16,  text="%", width=1, height=2, command=lambda: click("%")).grid(column=2, row=1)
bt18 = Button(master, bd=3, padx=16,  text="C", width=1, height=2, command=lambda: clear()).grid(column=3, row=1)
bt1 = Button(master, bd=3, padx=16,  text="7", width=1, height=2, command=lambda: click(7)).grid(column=0, row=2)
bt2 = Button(master, bd=3, padx=16,  text="8", width=1, height=2, command=lambda: click(8)).grid(column=1, row=2)
bt3 = Button(master, bd=3, padx=16,  text="9", width=1, height=2, command=lambda: click(9)).grid(column=2, row=2)
bt19 = Button(master, bd=3, padx=16,  text="/", width=1, height=2, command=lambda: click("/")).grid(column=3, row=2)
bt4 = Button(master, bd=3, padx=16,  text="6", width=1, height=2, command=lambda: click(6)).grid(column=0, row=3)
bt5 = Button(master, bd=3, padx=16,  text="5", width=1, height=2, command=lambda: click(5)).grid(column=1, row=3)
bt6 = Button(master, bd=3, padx=16,  text="4", width=1, height=2, command=lambda: click(4)).grid(column=2, row=3)
bt20 = Button(master, bd=3, padx=16,  text="*", width=1, height=2, command=lambda: click("*")).grid(column=3, row=3)
bt7 = Button(master, bd=3, padx=16,  text="3", width=1, height=2, command=lambda: click(3)).grid(column=0, row=4)
bt8 = Button(master, bd=3, padx=16,  text="2", width=1, height=2, command=lambda: click(2)).grid(column=1, row=4)
bt9 = Button(master, bd=3, padx=16,  text="1", width=1, height=2, command=lambda: click(1)).grid(column=2, row=4)
bt10 = Button(master, bd=3, padx=16,  text="-", width=1, height=2, command=lambda: click("-")).grid(column=3, row=4)
bt11 = Button(master, bd=3, padx=16,  text="0", width=1, height=2, command=lambda: click(0)).grid(column=0, row=5)
bt12 = Button(master, bd=3, padx=16,  text=".", width=1, height=2, command=lambda: click(".")).grid(column=1, row=5)
bt13 = Button(master, bd=3, padx=16,  text="=", width=1, height=2, command=lambda: equal()).grid(column=2, row=5)
bt14 = Button(master, bd=3, padx=16,  text="+", width=1, height=2, command=lambda: click("+")).grid(column=3, row=5)

master.mainloop()


# Finally done

print("\nDone")
