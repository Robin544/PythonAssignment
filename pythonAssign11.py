import threading
import time


# Create a threading process such that it sleeps for 5 seconds and then prints out a message.

def print_sleep():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(5)
    """
    sleep() is used to insert delay
    """
    print('Thread will wake up after 5 seconds and print the message.')

"""
Creating thread
"""
t = threading.Thread(name="First thread", target=print_sleep)
""" 
Starting the thread
"""
t.start()


# Make a thread that prints numbers from 1-10, waits for 1 sec between.

def print_num():
    for i in range(1, 11):
        print(threading.currentThread().getName(), i)
        time.sleep(1)


t = threading.Thread(name="Thread is printing : ", target=print_num)
t.start()


# Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a
# delay of multiple of 2 sec between each display. Delay goes like 2sec-4sec-6sec-8sec-10sec

def print_2n_delay():
    mylist = ["Robin", "Pooja", "Mayank", "Shalini", 5]
    j = 2
    for i in mylist:
        print(threading.currentThread().getName(), j,"seconds :", i)
        time.sleep(j)
        j = j + 2


t = threading.Thread(name="Element of list after delay of ", target=print_2n_delay)
t.start()


# Call factorial function using thread.

def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i
    print(threading.currentThread().getName(), fact)

time.sleep(22)
n = int(input("\nEnter the number to find the factorial : \n"))
t = threading.Thread(name="Factorial of the number : ", target=factorial, args=(n,))
t.start()


# Finally done

time.sleep(5)
print("\n\nDone")
