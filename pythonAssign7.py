
# Create a function to calculate the area of a circle by taking radius from user

def area(r):                # defining the function
    return 3.14*r*r

radius = float(input("\n Enter the radius of circle : "))
ans = area(radius)                               # calling the function
print(" Area of Circle with radius ", radius, " : ", ans, "sq.")




# Write a function “perfect()” that determines if parameter number is a perfect number
# Use this function in a program that determines and prints all the perfect numbers between 1 and 1000

pnList = list()             #  list to store perfect number

def perfect(num):              # defining function
    sum = 0
    for x in range(1, num):
        if num % x == 0:
            sum = sum + x
    if sum == num:
         pnList.append(num)

for numbr in range(1, 1001):
    perfect(numbr)              # calling perfect() for  numbers between 1 and 1000

print(" \nPerfect numbers between 1 and 1000 : ", pnList)




# Print multiplication table of 12 using recursion

def mul12(i):                          # defining function
    if (i < 11):
        print((" 12 x %d = %d") % (i, 12*i))
        mul12(i+1)
    else:
        print(" End of table of 12")

print("\n")
mul12(1)            # function calling




#  Write a function to calculate power of a number raised to other ( a^b ) using recursion

def pow_cal(base, pow):
    if pow != 0:
        return base*pow_cal(base, pow-1)       # multiply base value with its value pow times
    else:
        return 1

b = float(input("\n Enter Value of Base : "))
p = float(input(" Enter Value of Power : "))
ans_val = pow_cal(b,p)
print(" Value of ", b, "^", p, ":", ans_val)




# Write a function to find factorial of a number but also store the factorials calculated in a dictionary

def fact(n):
    if( n>=1):
        return n*fact(n-1)
    else:
        return 1

fact_dict = dict()
num = int(input("Enter the value to find factorial : "))
fact_ans = fact(num)

fact_dict[num]=fact_ans                     # storing factorial in dictionary in the form of " key : value "
print(" Factorial of ", num, " is ", fact_dict)


# Finally done
print("\n\nDone")