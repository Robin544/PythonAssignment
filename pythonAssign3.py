
# Create a list with user defined inputs


myList = list()
num = int(input("\nEnter the size of the list : "))
print("Enter items to list : ")
for i in range(num):
     item = input()
     myList.append(item)
print("List : ", myList)




# Add the following list to above created list:


myList.extend(['google', 'apple', 'facebook', 'microsoft', 'tesla'])
myList.append(['google', 'apple', 'facebook', 'microsoft', 'tesla'])
print("\nExtended List : ", myList)




# Count the number of time an object occurs in a list


item1 = input("\nEnter the item to be count : ")
count = myList.count(item1)
print(("Item occurs in list %d times : ") % (count))




# Create a list with numbers and sort it in ascending order


myList1 = list()
num1 = int(input("\nEnter the size of the list1 : "))
print("Enter items to list1 : ")
for i in range(num1):
     item1 = int(input())
     myList1.append(item1)
print("Unsorted List : ", myList1)
print("Sorted List in ascending order : ", sorted(myList1))




# To merge two arrays A and B into a single sorted array C, in ascending order


myList2 = list()
num2 = int(input("\nEnter the size of the list2 : "))
print("Enter items to list2 : ")
for i in range(num2):
     item2 = int(input())
     myList2.append(item2)
print("List 1 : ", myList1)
print("List 2 : ", myList2)

myList3 = myList1 + myList2              # Merging these list and then sorting
print("Merged List with items in ascending order : ", sorted(myList3))




#Implement a stack and queue using lists


     # Stack

myStack = ["Robin", "Pooja", "Singh", "Kamboj"]
myStack.append('Shalini')                             # Inserting item to the end(top) of Stack
myStack.append('Mayank')
print("\nStack after inserting item : ", myStack)
print("Deleted item : ", myStack.pop())                 # Deleting item form end(top) of Stack
print("Stack after deleting item : ", myStack)

    # Queue

myQueue = ["Robin", "Pooja", "Singh", "Kamboj"]
myQueue.append('Shalini')                               # Inserting item to the right(rear) of Queue
myQueue.append('Mayank')
print("Queue after inserting item : ", myQueue)
print("Deleted item : ", myQueue.pop(0))                  # Deleting item form left(front) of Queue
print("Queue after deleting item : ", myQueue)




# Count even and odd numbers in that list


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_e = 0
count_o = 0
for a in l:
    if a % 2 == 0:
        count_e = count_e+1
    else:
        count_o = count_o+1
print("\nList : ", l)
print("No. of even items in list", count_e)
print("No. of odd items in list", count_o)


# Finally Done
print("\nDone")