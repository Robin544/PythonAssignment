#                                          FILE HANDLING


# Importing 'random' library to get random numbers.

import random


# Write a Python program to read last n lines of a file.

with open("python-file-handling.txt", 'r') as f:
    read_line = f.readlines()
    """
    readlines() function is reading the lines till the end of file
    """

get_last_line = read_line[-1]
num = int(input("\nEnter the number of lines of a file for reading : "))
get_read_lines = read_line[-num:]
print(get_read_lines)


# Write a Python program to count the frequency of words in a file.

myList = []
with open("python-file-handling.txt", 'r') as f1:
    read_line = f1.readlines()
    for line in read_line:
        words = line.split()
        myList += words


input_word = input("\n\nEnter the word to count the frequency in a file : ")
x = myList.count(input_word)
print("'%s' has the frequency of : %d" % (input_word, x))


# Write a Python program to copy the contents of a file to another file.

with open('python-file-handling.txt', 'r') as f2, open('git-commands.txt', 'w') as f3:
    for line in f2:
        f3.write(line)


# Write a Python program to combine each line from first file with the corresponding line in second file.

print("\n\n")
with open('python-file-handling.txt', 'r') as f4, open('git-commands.txt', 'r') as f5:
    for line1, line2 in zip(f4, f5):        # line1, line2 for f4, f5 respectively.
        """
        Here, this will take line1 from f4 will combine with line2 from f5 and
        then print the output in the combined form.
        """
        output = line1 + line2
        print(output)


# Write a Python program to write 10 random numbers into a file.
# Read the file and then sort the numbers and then store it to another file.

my_list = []
ram_num = int(input('\n\nEnter the random numbers : '))
with open('random_numbers.txt', 'w') as f6:
    for i in range(ram_num):
        line = str(random.randint(1, 1000))
        f6.write(line + '\n')


with open('random_numbers.txt', 'r') as f6:
    get_lines = f6.readlines()
    for line in get_lines:
        print(line)
        my_list.append(line)


my_list.sort()
with open('sorted_numbers.txt', 'w') as f7:
    for j in my_list:
        f7.write(j)


# Finally done

print("\n\nDone")
