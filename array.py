# Q1: Monotonic Array (896)

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

# Test Cases:

# Input: [1,2,2,3]
# Output: true
# Example 2:

# Input: [6,5,4,4]
# Output: true
# Example 3:

# Input: [1,3,2]
# Output: false
# Example 4:

# Input: [1,2,4,5]
# Output: true
# Example 5:

# Input: [1,1,1]
# Output: true


# Thoughts:
# Has to be in order, sorted
# Check if the list is ordered
# Check if i <= j, then continue
# Check if i >= j, then continue

# Special cases:
# I: []
# O: false

# I: [0]
# O: false

# Pseudocode:

# Iterate through the list
# If i[0] <= i[0+1], continue


# else, return false

# Iterate through the list
# If i[0] >= i[0+1], continue

# else, return false


# return true

# Code:


# class Solution:
#     def isMonotonic(self, A: List[int]) -> bool:

#         if A[0] <= A[1]:
#             for i in range(len(A) - 1):
#                 if A[i] <= A[i + 1]:

#                     continue

#                 else:
#                     return False

#         if A[0] >= A[1]:
#             for i in range(len(A) - 1):
#                 if A[i] >= A[i + 1]:

#                     continue

#                 else:
#                     return False


# ======================
# class Solution:
#     def isMonotonic(self, A: List[int]) -> bool:

#         return all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(
#             A[i] >= A[i + 1] for i in range(len(A) - 1)
#         )


# Notes:
# Passing in a list
# once the first check between A[i] and A[i+1] is done in the first iteration, then # all() returns True
# print(all([True]))
# Output: True

# lst1 = [True]

# print(lst1) #output: [True]
# print(all(lst1)) #output: True

# =================

# class Solution:
#     def isMonotonic(self, A: List[int]) -> bool:


#         increasing = decreasing = True  #Assigning two variables here

#         for i in range(len(A) - 1):
#             if A[i] > A[i+1]:
#                 increasing = False
#             if A[i] < A[i+1]:
#                 decreasing = False

#         return increasing or decreasing  #if one is True, it'll return True

# Input: [1,3,2]
# Output: false
# Example 4:

# Input: [1,2,4,5]
# Output: true
# Example 5:

# Input: [1,1,1]
# Output: true

a = b = c = True
print(a)
print(b)
print(c)

print(3 > 5)

