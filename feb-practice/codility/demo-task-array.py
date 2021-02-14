# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


# THoughts/Pseudo:
# Has to be greater than 0
# Put the list into a set to remove duplicates
# Create a list wiht range 1 to 100,000
# Iterate through the set as a list
# If the number is not in the range, reuturn the number. Make sure it isn't 0


# Code
def solution(A):
    set_lst = list(set(A))  # [1, 2, 3, 4, 6]

    if A == []:
        return 1

    for i in range(1, 100001):
        if i not in set_lst and i > 0:
            return i


print(solution([1, 3, 6, 4, 1, 2]))

print(solution([1, 2, 3]))

print(solution([-1, -3]))

print(solution([]))

print(solution([-1, -3, 6, -4]))
