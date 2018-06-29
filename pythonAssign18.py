#                                       STATISTICS AND NUMPY


# Importing numpy library.
import numpy as np
# Now we will use 'np' instead of 'numpy'.


# QUESTION 1:
# Create a numpy array with 10 elements of the shape(10, 1) using np.random and
# find out the mean of the elements using basic numpy functions.

my_array = np.random.rand(10, 1)
print("\nNumpy array with 10 elements of the shape(10, 1):\n", my_array)
print("\nMean of the numpy array elements: ", np.mean(my_array))


# QUESTION 2:
# Create a numpy array with 20 elements of the shape(20, 1) using np.random and
# find the variance and standard deviation of the elements.

my_array1 = np.random.rand(20, 1)
print("\n\nNumpy array with 20 elements of the shape(20, 1):\n", my_array1)

# Calculating the standard deviation using numpy library function(np.std(array)).
print("\nStandard deviation of elements in array: ", np.std(my_array1))
# Calculating the variance using numpy library function(np.var(array)).
print("Variance of elements in array: ", np.var(my_array1))


# QUESTION 3:
# Create a numpy array A of shape(10, 20) and B of shape (20, 25) using np.random.
# Print the matrix which is the matrix multiplication of A and B.
# The shape of the new matrix should be (10, 25).
# Using basic numpy math functions only
# find the sum of all the elements of the new matrix.

array_A = np.random.rand(10, 20)
print("\n\nNumpy array A of shape(10, 20):\n", array_A)
array_B = np.random.rand(20, 25)
print("\nNumpy array B of shape(20, 25):\n", array_B)

# Calculating the matrix multiplication using numpy library function(np.dot(a, b)).
matrix_multiplication = np.dot(array_A, array_B)
print("\nMatrix multiplication of array A and array B:\n", matrix_multiplication)

print("\nSum of all the elements of the new matrix: ", np.sum(matrix_multiplication))


# QUESTION 4:
# Create a numpy array A of shape(10, 1).
# Using the basic operations of the numpy array generate an array of shape(10, 1)
# such that each element is the following function applied on each element of A.
#       f(x) = 1 / (1 + exp(-x))
# Apply this function to each element of A and print the new array holding the value the function returns
# Example:
#       a = [a1, a2, a3]
#       n(new array to be printed ) = [ f(a1), f(a2), f(a3)]

array_A1 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print("\n\nNumpy array A of shape(10, 1):\n", array_A1)


def function1(x):
    return 1 / (1 + np.exp(-x))


new_array = function1(array_A1)
print("\nAfter applying function to each element of array A, the new array to be printed:\n", new_array)


# Finally done

print("\n\nDone")
