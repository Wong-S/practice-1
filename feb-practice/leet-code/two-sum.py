# Two Sum (1)

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Input: nums = [0,4,3,0] , target = 0
# Output: [0,3]


# Thoughts:
# Since we only have one element, no repeat, place in a set
# Convert set back to list
# Empty list to hold indices
# Iterate through the list
# Check if the num is not equal or greater than target
# Iterate the list again but start at the second
# If the nums add to target,
# append indices of nums to new list
# Return the list
#

# Instead of a set, use dict

# Code
from collections import defaultdict


def twoSum(nums, target):

    indice_lst = []

    for indx, num in enumerate(nums):
        print("The current index is", indx)

        for n in range(len(nums)):
            print(n)
            print(num)
            print(nums[n])
            if num + nums[n] == target and indx != n:  # index at 0 !=
                indice_lst.append(indx)
                indice_lst.append(n)

                return indice_lst


print(twoSum([2, 7, 11, 15], 9))

