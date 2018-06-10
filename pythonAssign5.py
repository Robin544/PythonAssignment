# Take an input year from user and decide whether it is a leap year or not

year = int(input("\nEnter the year you want to check : "))
if(year % 400 == 0):
    print("Leap year")
elif(year % 100 != 0 and year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")


#  Take length and breadth input from user and check whether the dimensions are of square or rectangle

length=int(input("\nEnter Length : "))
breadth=int(input("Enter Breadth : "))
if(length == breadth):
    print(" Dimensions are Equal so  Square ")
else:
    print(" Dimensions are Not Equal so Rectangle ")


#   Take the input age of 3 people and determine oldest and youngest among them

age1 = int(input("\nEnter Age of First person : "))
age2 = int(input("Enter Age of Second person : "))
age3 = int(input("Enter Age of Third person : "))
if (age1 == age2  == age3):
    print("\nAll persons are of same age")
else:
    a = max(age1,age2,age3)
    b = min(age1,age2,age3)
    print(("\nPerson having age %d is Oldest among three") % (a))
    print(("Person having age %d is Youngest among three") % (b))


# Write an if statement that lets a competitor know which of the prizes they won

points = int(input("\nEnter points between 1 to 200 :"))
if(1 <= points <= 50):
    print("No Prize")
elif(51 <= points <= 150 ):
    print("Wooden Dog")
elif(151 <= points <= 180 ):
    print("Book")
elif(181 <= points <= 200 ):
    print("Chocolates")
elif(points >= 200):
    print("Please enter the valid points")


# A shop will give discount of 10% if the cost of purchased quantity is more than 1000
# Judge and print total cost for user

cost = int(input("\nEnter the cost of purchased quantity : "))
if( cost >= 1000):
    dis = cost * 0.1
    print("Discount : ", dis)
    total_cost = cost - dis
else:
    total_cost = cost
print("Total cost : " ,total_cost )


#Finally done
print("\n\nDone")