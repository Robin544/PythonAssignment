# Let’s lookout some interesting methods and properties of the commonly used packages


# What is Time Tuple?

file_name = "time_tuples.txt"
file = open(file_name, "r")
for i in file:
   print(i)


# Write a program to get formatted time


import time
t = time.asctime(time.gmtime())
print("\n\nCurrent time : ", t)


# Extract month from the time

import datetime
m = datetime.date.today()
x = m.month
x1 = m.strftime("%B")
print(("\nCurrent month : %02d (%s)")%(x, x1))


# Extract day from the time

d = m.day
d1 = m.strftime("%A")
print(("\nCurrent day : %02d (%s)")%(d, d1))


# Extract date (ex : 11 in 11/01/2021) from the time

print("\nCurrent date : ", m.strftime("%d-%m-%Y"))
print("Extract only day : ", m.day)


# Write a program to print time using localtime method

local_time = time.asctime( time.localtime(time.time()) )
print("\nLocal current time :", local_time)


# Find the factorial of a number input by user using math package functions

import math

num = int(input("\n\nEnter a number to find the factorial : "))
f_num = math.factorial(num)                    # find the factorial using the factorial function of math library
print(("Factorial of %d : %d")%(num, f_num))


# Find the GCD of a number input by user using math package functions

a = int(input("\n\nEnter Ist number for greatest common divisor : "))
b = int(input("Enter IInd number for greatest common divisor : "))
ab_gcd = math.gcd(a, b)
print(("\nThe greatest common divisor for (%d,%d) is %d")%(a, b, ab_gcd))



# Use OS package and do the following tasks:

#1. Get current working directory
import os

op_sys = os.getcwd()
print(("\n\nYour current working directory is %s ")%(op_sys))

#2. Get the user environment

print("\n", os.environ)
print("\n", os.environ['PATH'])
#print("\n", os.environ['HOME'])


# Finally done
print("\n\nDone")