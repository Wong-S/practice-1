# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

# Write a function:

# def solution(A, K)

# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

# For example, given

#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:

#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given

#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]

# Given

#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]

# Assume that:

# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

# Thought/Pseudo

# Given K, do a reverse splice in that list to take out what last numbers will be placed in front
# Iterate through the original list and keep adding elements until it reaches the first element in the spliced list
# Return the completed/shifted list


# Code:
def shift_list(arr, k):

    shifted_lst = arr[-k:]  # [9,7,6]

    for index, num in enumerate(arr):
        if (
            index == (k - 1) and num == shifted_lst[0]
        ):  # NOTE: The last index in the list, if reading in reverse, is NOT 0, but -1
            break
        else:
            shifted_lst.append(num)

    # Checking if the lengths of the new array is same as old array
    if len(arr) == len(shifted_lst):
        return shifted_lst

    else:
        return arr


print(shift_list([3, 8, 9, 7, 6], 3))

print(shift_list([0, 0, 0], 1))

print(shift_list([1, 2, 3, 4], 4))

print(shift_list([4, 2, 3, 4, 7, 1], 3))

# ===================================
# Alternative Method to pass the last test case that I made above.....
# use the length instead and splice method. Only passes 75 percent
def shift_list(arr, k):

    # Edge case:
    if k == 0:
        return arr

    shifted_lst = arr[-k:]  # [9,7,6] , [0] , [1,2,3,4]

    splice_i = len(arr) - k
    remaining_num_lst = arr[:splice_i]

    combine_lst = shifted_lst + remaining_num_lst
    return combine_lst


print(shift_list([3, 8, 9, 7, 6], 3))

print(shift_list([0, 0, 0], 1))

print(shift_list([1, 2, 3, 4], 4))

print(shift_list([4, 2, 3, 4, 7, 1], 3))

print(shift_list([-4], 0))  # [-4]   #Edge Case: K = 0

print(shift_list([1, 1, 2, 3, 5], 42))  # [3,5,1,1,2]  #Edge case: K >= N
# EDGE CASES:
# THINGS TO THINK ABOUT: One, None, Many , NEGATIVE numbers

# ===================Alt method......100% pass
def shift_list(A, K):

    # Edge case:
    if K == 0 or A == []:
        return A

    count = 0
    shifted_lst = []
    while count < K:
        # Take last element and insert in front of list
        last_ele = A.pop()

        # Insert into front of list
        A.insert(0, last_ele)

        count += 1

    return A


print(shift_list([3, 8, 9, 7, 6], 3))

print(shift_list([0, 0, 0], 1))

print(shift_list([1, 2, 3, 4], 4))

print(shift_list([4, 2, 3, 4, 7, 1], 3))

print(shift_list([-4], 0))  # [-4]   #Edge Case: K = 0

print(shift_list([1, 1, 2, 3, 5], 42))  # [3,5,1,1,2]  #Edge case: K >= N

print(shift_list([], 1))
# EDGE CASES:
# THINGS TO THINK ABOUT: One, None, Many , NEGATIVE numbers
