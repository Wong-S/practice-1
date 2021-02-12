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
    # =================================================================
    new_binary_str = ""

    dict_a = {}
    count_a = 1
    for i in a:
        dict_a[count_a] = i
        count_a += 1
    print(dict_a)
    # =================================================================
    x = defaultdict(list)
    y = 1
    for i in a:
        x[y].append(i)  # for the LIST, you need to put append.
        y += 1

    print(x)  # defaultdict(<class 'list'>, {1: ['1'], 2: ['1']})
    # =================================================================
    x = defaultdict(int)
    y = 1
    for i in a:
        x[y] = i  # for int, no need for append
        y += 1

    print(x)  # defaultdict(<class 'list'>, {1: ['1'], 2: ['1']})
    # =================================================================

    x = defaultdict(str)
    y = 1
    for i in a:
        x[y] = i  # for int, no need for append
        y += 1

    print(x)  # defaultdict(<class 'str'>, {1: '1', 2: '1'})
    # =================================================================
    # NOTE: This below is similar to using the Counter method. So it'll count the occurrences for each key
    # Can also use the .get() method if you aren't using collections dictionary. Notice you'll need ot use an int class. As string cannot add those int numbers
    x = defaultdict(int)

    for i in a:
        x[i] += 1  # for int, no need for append

    print(x)  # defaultdict(<class 'int'>, {'1': 2})


addBinary("11", "1")

# ==================================================
# ==================================================
# CODING PORTION:

a = "11"
b = "1"
# Output: "100"
# Example 2:
def binary_addition(str1, str2):
    dict_1 = defaultdict(int)


binary_addition("11", "1")


def add_binary(a, b):
    if len(a) >= len(b):
        a = a
        b = b

    else:
        a = b
        b = a

    carry_int = 0

    binary_lst = []  # [0,0,1] --> 100

    # for indx, char in enumerate(str1[::-1]):
    #     print (char)
    #     print(int(str2[indx -1]))  #1 --> KEEPS GOINT AT INDEX [-1] so repeats last element

    for index, char in enumerate(a[::-1]):
        if carry_int != 1:
            total_sum = int(char) + int(b[index - 1])
        else:
            print(char)
            print(int(b[index - 1]))  # 1 instead of 0
            total_sum = int(char) + int(b[index - 1]) + carry_int

        if total_sum > 2:
            if carry_int == 1:
                binary_lst.append("1")
            else:
                carry_int = 1
                binary_lst.append("0")

        elif total_sum == 2:

            # if carry_int == 1:
            #     carry_int = 1
            #     binary_lst.append("1")
            # else:
            carry_int = 1
            binary_lst.append("0")

        elif total_sum == 0:  # 0,1,2
            if carry_int == 1:
                total_sum += carry_int
                binary_lst.append(str(total_sum))

            else:
                binary_lst.append("0")

        elif total_sum == 1:
            if carry_int == 1:

                binary_lst.append("0")

            else:
                binary_lst.append("1")

    if carry_int == 1:
        binary_lst.append("1")

    # This step converts the string list into a string final type. Note: If you use an int list instead of string, it'll not join properly! It must be converted to string!
    binary_str = ""
    binary_lst.reverse()
    return binary_str.join(binary_lst)


print(add_binary("1", "111"))


# ==================================================
# ==================================================
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


# ==================================================
# ==================================================
# import collections

# def gridIllumination(N, lamps, queries):
#     """
#     :type N: int
#     :type lamps: List[List[int]]
#     :type queries: List[List[int]]
#     :rtype: List[int]
#     """
#     col = collections.defaultdict(int)
#     row = collections.defaultdict(int)
#     diag1 = collections.defaultdict(int)
#     diag2 = collections.defaultdict(int)
#     lamps = set((i, j) for i, j in lamps)

#     for i, j in lamps:
#         col[j] += 1
#         row[i] += 1
#         diag1[i - j] += 1
#         diag2[i + j] += 1

#     res = []
#     for i, j in queries:
#         res.append(
#             int(row[i] > 0 or col[j] > 0 or diag1[i - j] > 0 or diag2[i + j] > 0)
#         )
#         for di in [-1, 0, 1]:
#             for dj in [-1, 0, 1]:
#                 ni, nj = i + di, j + dj
#                 if ni < 0 or ni >= N or nj < 0 or nj >= N:
#                     continue
#                 if (ni, nj) in lamps:
#                     row[ni] -= 1
#                     col[nj] -= 1
#                     diag1[ni - nj] -= 1
#                     diag2[ni + nj] -= 1
#                     lamps -= {(ni, nj)}
#     print(res)
#     return res


# print(gridIllumination(8, [[4, 3], [4, 4]], [[3, 4], [7, 6]]))

