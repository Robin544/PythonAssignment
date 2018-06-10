#Let’s play with tuples ,sets and dictionaries


#TUPLES

#Create a tuple with different data types
myTuple = (1, 2, 3, 'Pooja', 'Robin')
print("\nTuple : ", myTuple)

#Find the length of tuples
print("\nLength of Tuple : ", len(myTuple))

#Find largest and smallest elements of a tuples
myTuple1 = (1,2,3,4,5)
print("\nTuple : ", myTuple1)
print("Largest in Tuple : ", max(myTuple1))
print("Smallest in Tuple : ", min(myTuple1))

#Find the product of all elements of a tuple
prod = 1
for x in myTuple1:
    prod = prod*x
print("\nTuple : ", myTuple1)
print("Product of Tuple's elements : ", prod)


#SETS

#Create two set using user defined values

s1 = set()              #Set1
num = int(input("\n\nEnter the no. of elements of Set1 : "))
print("Enter elements to set : ")
for i in range(num):
    elem=input()
    s1.add(elem)
print("Set1 : ", s1)

s2= set()               #Set2
num1 = int(input("\nEnter the no. of elements of Set2 : "))
print("Enter elements to set : ")
for i in range(num1):
    elem1=input()
    s2.add(elem1)
print("Set2 : ", s2)

#Calculate difference between two sets
print("\nDifference of Set1 and Set2 : ", s1 - s2)
print("Difference of Set2 and Set1 : ", s2 - s1)

#Print the result of intersection of two sets
print("\nIntersection of Set1 and Set2 :", s1 & s2)

#Compare two sets
if(s1<=s2):
    print("\nSet2 is superset")
elif(s1>=s2):
    print("\nSet2 is subset of Set1")
else:
    print("\nSets are different")


#DICTIONARIES

#Create a dictionary to store name and marks of 10 students by user input
myDict = dict()
print("\n\nEnter elements to dictionary as Key:Value pair : ")
for i in range(10):
    key = input()
    value = int(input())
    myDict[key] = value
print("\nUnsorted Dictionary is : ", myDict)

#Sort the dictionary created in previous question according to marks
sort_x = sorted(myDict.items(), key=lambda x: x[1])
print("\nSorted Dictionary is : ", sort_x)


#Count the number of occurrence of each letter in word "MISSISSIPPI"
word = "MISSISSIPPI"
from collections import Counter
count_word = Counter(word)
print("\nOccurance of each letter : ", count_word)

#Finally Done
print("\nDone")