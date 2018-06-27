#                                  Graphical User Interface

# Importing tkinter

from tkinter import *


# Write a python program using tkinter interface to write Hello World and
# a exit button that closes the interface.

master = Tk()
master.title("Basic Graphical User Interface")
master.pack_slaves()
"""
we can use master.geometry('X x Y') instead of master.pack_slaves(),
that also will create a given parameterised window as a parent.
"""
label = Label(master, text="Hello World!")
label.grid(row=2, column=15)
"""
Label is just a text in english which will be printed on the window(parent).
"""
button = Button(master, text="Exit", command=master.destroy)
button.grid(row=15, column=15)
"""
Button() function will create a button to trigger an event.
"""


# Write a python program to in the same interface as above and
# create an action when the button is clicked, it will display some text.

def button_clicked():
    label_1 = Label(master, text="Button is clicked successfully!")
    label_1.grid(row=12, column=15)


button_2 = Button(master, text="Click Me", command=button_clicked)
"""
button_clicked() function is used to trigger an event when button is clicked.
"""
button_2.grid(row=7, column=15)
master.mainloop()       # this(mainloop) is for itration and exit from the window


# Create a frame using tkinter with any label text and two buttons.
# One to exit and other to change the label to some other text.

master1 = Tk()
master1.title("Frame GUI")
frame = Frame(master1)
"""
This will create a frame with parent window(master1)
"""
frame.pack()
label_2 = Label(frame, text="Hello World!")
label_2.grid(row=0, column=0)
button_2 = Button(frame, text="Exit", command=master1.destroy)
button_2.grid(row=8, column=0)


def button_clicked1():
    label_2.configure(text="label is overwritten successfully!")
    label_2.grid(row=6, column=0)


button_3 = Button(frame, text="Change Label", command=button_clicked1)
button_3.grid(row=3, column=0)

master1.mainloop()


# Write a python program using tkinter interface to take an input in the GUI program and print it.

master3 = Tk()
master3.title("Input GUI")
master3.pack_slaves()
"""
We can use geometry instead of pack_slaves() function.
"""
label_3 = Label(master3, text="Enter any input : ")
label_3.grid(row=0, column=0)
entry = Entry(master3, width=20)
entry.grid(row=0, column=2)


def button_clicked2():
    output = entry.get()
    if entry.get() != "":
        label_4 = Label(master3, text="Your entered input is : " + output)
        label_4.grid(row=5, column=2)
    else:
        label_4 = Label(master3, text="Please enter any input!")
        label_4.grid(row=8, column=2)


button = Button(master3, text="Check Input", command=button_clicked2)
button.grid(row=2, column=2)
master3.mainloop()


# Finally done

print("\nDone")
