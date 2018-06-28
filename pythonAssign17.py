#                                          GUI 2


# Create a dict with name and mobile number.
# Define a GUI interface using tkinter and pack the label and
# create a scrollbar to scroll the list of keys in the dictionary.

from tkinter import *
import re


master = Tk()
master.title("GUI2")
frame = Frame(master)
frame.pack()
label = Label(frame, text="Graphical User Interface")
label.pack()
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
my_dict = {"Robin Singh": 9812345616, "Pooja Kamboj": 9812345619, "Shalini": 9812345622,
           "Mayank": 9812345610, "Yakshay": 9812345621, "Prashant": 9812345625,
           "Shivani": 9812345612, "Sahil": 9812345615, "Sourbh": 9812345606,
           "Jyoti": 9812345619, "Nitya": 9812345602, "Ashish Kumar": 9812345601,
           "Parvesh": 9812345607, "Ashok": 9812345614, "Gyan Singh": 9812345604}

my_list = Listbox(frame, yscrollcommand=scrollbar.set)
for line in my_dict:
    my_list.insert(END, str(line))

my_list.pack(side=RIGHT, fill=BOTH)
scrollbar.config(command=my_list.yview)


# In the same tkinter file as created above, create a function to insert items into the dictionary.

def insert_key_value():
    """
    this function is used to insert new key(Name) :value(Phone_Number) pairs to dictionary.
    :return:
    It will return a new dictionary with inserted elements.
    """
    key = ""
    my_dict.update({insert_name.get(): insert_ph_number.get()})

    def is_valid(n):        # This function will check the phone number is valid or not.

        # 1) Begins with 0 or 91
        # 2) Then contains 7 or 8 or 9.
        # 3) Then contains 9 digits
        pattern = re.compile("[v]?[7-9][0-9]{9}")
        return pattern.match(n)

    # Driver Code
    s = insert_ph_number.get()

    # These are the conditions to check whether all fields are correct or not.
    if insert_name.get() == "" or insert_ph_number.get() == "":
        txt = Text(frame, height=5, width=20)
        txt.pack()
        txt.insert(END, "Both fields are mandatory!")
    elif is_valid(s):
        for key in my_dict.keys():
            print(key)
        my_list.insert(END, key)
    else:
        txt = Text(frame, height=5, width=20)
        txt.pack()
        txt.insert(END, "Please enter valid phone number!")


label_1 = Label(frame, text="Enter the name: ")
label_1.pack()

insert_name = Entry(frame)      # Entry field to enter the name.
insert_name.pack()

label_1 = Label(frame, text="Enter the phone number: ")
label_1.pack()

v = StringVar(frame, value='91')
insert_ph_number = Entry(frame, textvariable=v)     # Entry field to enter the phone number.
insert_ph_number.pack()

insert_button = Button(frame, text="Insert", command=insert_key_value)
insert_button.pack()

master.mainloop()


# Finally done

print("\nDone")
