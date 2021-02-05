# Prompt: Given two binary strings a and b, return their sum as a binary string.

# Test Cases:
# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# Thought/Pseudo:
# We know that for binary, if the sum of the digits is greater than 1, then carry over and append 0.
# [1 , 1]
# [0 , 1]

# Create a new variable to hold the string
# convert strings into integers
# Put the first list into a hash map/dict
# put the second list into a dictionary

# Iterate over the first dictionary backwards and compare to the second dict by add the values of the keys. If the value is greater than 1 (ie equal to 2),
# then carry over and append 0 to the new string via concatenation. Else, append 1.

# ==================================================
# ==================================================
# NOTES: Below is showing different ways to make a dict with unique key values
# First method is how you might do it without collections library
# Second and third method is using the collections method! Notice passing in a list class or int class

import sys
from collections import Counter, defaultdict


def addBinary(a: str, b: str) -> str:

    new_binary_str = ""

    dict_a = {}
    count_a = 1
    for i in a:
        dict_a[count_a] = i
        count_a += 1
    print(dict_a)

    x = defaultdict(list)
    y = 1
    for i in a:
        x[y].append(i)  # for the LIST, you need to put append.
        y += 1

    print(x)  # defaultdict(<class 'list'>, {1: ['1'], 2: ['1']})

    x = defaultdict(int)
    y = 1
    for i in a:
        x[y] = i  # for int, no need for append
        y += 1

    print(x)  # defaultdict(<class 'list'>, {1: ['1'], 2: ['1']})


addBinary("11", "1")

# ==================================================
# ==================================================

