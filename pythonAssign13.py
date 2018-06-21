# Name and handle the exception occurred in the following program:

a = 3
try:
    if a < 4:
        """
        As a is 3 so 3/0 will create an exception so except block will be execute. 
        """
        a = a/(a-3)

except ZeroDivisionError:
    print("\nYou are trying to perform division using 0")

else:
    print(a)


#  Name and handle the exception occurred in the following program:

try:
    mylist = [1, 2, 3]
    print(mylist[3])

except IndexError:
    print("\n\nOut of range error as list has 0 to 2 indices\n"
          "You are trying to print element at 3 index which is not possible")


# What will be the output of the following code.

try:
    """
    This will raise a NameError and except block will execute in its response
    """
    raise NameError("Hi there ! ")
except NameError:
    print("\n\nAn exception occurred")


# What will be the output of the following code:

def add_div(aa, bb):
    try:
        a1 = aa
        b1 = bb
        c = ((a1+b1) / (a1-b1))
    except ZeroDivisionError:
        print("As a and b are equal in magnitude, divide by zero exception occurs")
    else:
        print("\n\nAnswer : ", c)


"""
Here a and b has different values i.e.,a-b will not result in 0 so no exception will occurs and else block will execute
"""
add_div(2.0, 3.0)
"""
Here a and b has same value i.e.,a-b will result in 0 so an exception will occurs and except block will execute
"""
add_div(3.0, 3.0)


# Write a program to show and handle following exceptions:
# 1. Import Error

try:
    import abc
    raise ImportError()
except ImportError:
    print("\n\nYou are trying to import an undefined library")

# 2. Value Error

try:
    a = input("\nEnter Number:")
    """
    This will raise an exception if input is not a digit
    """
    if not a.isdigit():
        raise ValueError()
except ValueError:
    print("Please enter only a number")
else:
    print("Success")

# 3. Index Error

my_list = [1, "a", 3, 4, "n"]
try:
    """
    AS mylist has only 0 to 4 indices an exception will occur on accessing element at index 7
    """
    print(my_list[7])
except IndexError:
    print("\nOut of bound")


# Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
# The code must keep taking input till the user enters the appropriate age number(less than 18).

class AgeTooSmallError(Exception):
    pass


def take_input(age_of):
        if age_of < 18:
            raise AgeTooSmallError()
        else:
            print("Done!")


age = 0
while age < 18:
    try:

        age = int(input("\n\nEnter age : "))
        take_input(age)

    except AgeTooSmallError:
        print("Age is less than 18 \n"
              "Please enter valid age")
