
# Take 10 integers from user and print it on screen

myList = list()
print("\nEnter values to List : ")
for i in range(10):
    int_val = int(input(("Enter %d value : ") %(i+1)))  # Taking input from user
    myList.append(int_val)
print("Integer List : " ,myList)



# Write an infinite loop.An infinite loop never ends. Condition is always true

while range(10):         # Condition is always true
    print("It is an infinite loop : ")


#Create a list of integer elements by user input
#Make a new list which will store square of elements of previous list

myList1 = list()
myList2 = list()
print("\n\nEnter values to List to find Square List: ")
for a in range(5):
    int_val1 = int(input(("Enter %d value : ") %(a+1)))
    myList1.append(int_val1)        # a list of integer
print("Integer List : " ,myList1)
for item in myList1:
    sq_val = item*item
    myList2.append(sq_val)          # a list of square of elements
print("Square List : " ,myList2)


# From a list containing ints, strings and floats, make three lists to store them separately

myList3 = [ 1,2,3,"a", "b", 1.5,1.6, 1.7, 8]
int_List = [ i  for i in myList3 if isinstance(i, int) ]
str_List = [ i  for i in myList3 if isinstance(i, str) ]
float_List = [ i  for i in myList3 if isinstance(i, float) ]
print("\n\nMixed List : " , myList3)
print("Integer List : " ,int_List)
print("String List : " ,str_List)
print("Float List : " ,float_List)


# Using range(1,101), make a list containing even and odd numbers.

eList = list()
oList = list()
for li in range(1,101):
    if(li % 2 == 0):
        eList.append(li)
    else:
        oList.append(li)
print("\nEven List : ", eList)
print("Odd List : ", oList)


 #Print the pattern

pattern = '*'
print("\n\n")
for i in range(1,5):
    print(pattern*i)


# Create a user defined dictionary and get keys corresponding to the value using for loop

myDict = dict()
print("\n\nEnter elements to dictionary as Key:Value pair : ")
for i in range(5):
    key = input(("Enter key %d") % (i+1))
    value = input(("Enter Value of %d key") % (i+1))
    myDict[key] = value
for it in myDict:
    print(it,':',myDict[it])


 # Take inputs from user to make a list. Again take one input from user and
# search it in the list and delete that element, if found. Iterate over list using for loop.

num = int(input('\n\nEnter the length of List : '))
user_list = list()
print("Enter the elements to List : ")
for x in range(num):
    in_val = input()
    user_list.append(in_val)
print(" List : ", user_list)
del_item = input(("Enter the input to delete : "))
if( del_item in user_list):
    user_list.remove(del_item)
    print(" List after deletion : ", user_list)
else:
    print("Input value is not in List")

    
# Termination of code
print("\n\nEnd of code")
