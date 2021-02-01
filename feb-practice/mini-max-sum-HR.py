# Prompt:
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Test Cases"
# I: arr = [1,3,5,7,9]
# O: 16, 24
# Minimum sum is 1 + 3 + 5 + 7 = 16
# Maximum sum is 3 + 5 + 7 + 9 = 24

# I: arr = [1,2,3,4,5]
# O: 10, 14

# Unintentional Cases:
# WIll the array always be sorted?
# Always positive integers?
# Floats?
# Always a integer?

# Pseudo/Thought
# Using the window-slide method

# Create a function with one parameter (LIST)
#     assign windowStart and windowSum to zero
#     Iterate through the entire array via range(len)
#         Get the windowSum by adding the element each time

#     Once the windowSum is found, to find the max, subtract the first element from the sum
#         Assign this to a variable
#     Once the windowSum is found, to find the min, subtract the last element from the sum
#         Assign this min value to a variable

#     Return the min and max value


# NVM:
# Just iterate and find the sum. NO need for window-slide method

# Note: The elements in the array may not be in order, so must be sorted

# Code:
def min_max_sum(arr):
    windowSum = 0

    arr_sorted = sorted(arr)
    for num in arr_sorted:
        windowSum += num

    max_num = windowSum - arr_sorted[0]
    min_num = windowSum - arr_sorted[-1]

    print(
        min_num, max_num
    )  # Returns a tuple (min_num, max_num) if you use return() instead of print()


# Call the function:
min_max_sum([1, 3, 5, 7, 9])

min_max_sum([7, 69, 2, 221, 8974])

