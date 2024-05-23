import numpy as np

# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Create a function (create_numpy_array) that takes a list of numbers and returns a NumPy array.
"""

### YOUR CODE HERE:
def create_numpy_array(p_list):
    return np.array(p_list)
### TEST:
print(create_numpy_array([1, 2, 3, 4, 5]))

### EXPECTED OUTPUT:
# [1 2 3 4 5]

# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a function (array_sum) that takes a NumPy array and returns the sum of its elements.
"""

### YOUR CODE HERE:
def array_sum(arr):
    return np.sum(arr)
### TEST:
print(array_sum(np.array([1, 2, 3, 4, 5])))

### EXPECTED OUTPUT:
# 15


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Create a function (evens_in_array) that takes a NumPy array and returns a new array containing only the even numbers.
"""

### YOUR CODE HERE:
def evens_in_array(arr):
    filter = arr%2 == 0
    return arr[filter]
### TEST:
print(evens_in_array(np.array([1, 2, 3, 4, 5, 6])))

### EXPECTED OUTPUT:
# [2 4 6]


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a function (count_greater_than) that takes a NumPy array and a threshold value, and returns the count of elements greater than the threshold.
"""

### YOUR CODE HERE:
def count_greater_than(arr, f):
    return np.count_nonzero(arr>f)
### TEST:
print(count_greater_than(np.array([1, 2, 3, 4, 5]), 3))

### EXPECTED OUTPUT:
# 2


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Create a function (access_element) that takes a NumPy array and an index, and returns the element at that index.
"""

### YOUR CODE HERE:
def access_element(arr, i):
    return arr[i]
### TEST:
print(access_element(np.array([10, 20, 30, 40, 50]), 3))

### EXPECTED OUTPUT:
# 40


# ---------------------------------- Task 6 ---------------------------------- #
""" DESCRIPTION:
Create a function (slice_array) that takes a NumPy array and two indices, start and end, and returns the sliced array.
"""

### YOUR CODE HERE:
def slice_array (arr, from_i, to_i):
    return  arr[from_i:to_i]
### TEST:
print(slice_array(np.array([10, 20, 30, 40, 50]), 1, 4))

### EXPECTED OUTPUT:
# [20 30 40]
