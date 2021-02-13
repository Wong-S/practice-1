# 653. Two Sum IV - Input is a BST

# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Ex1:
#         5
#      /     \
#     3       6
#    /  \       \
#   2   4        7
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true


# Ex2:
#         5
#      /     \
#     3       6
#    /  \       \
#   2   4        7

# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

# Ex 3:
# Input: root = [2,1,3], k = 4
# Output: true

# Ex 4:
# Input: root = [2,1,3], k = 1
# Output: false

# Ex 5:
# Input: root = [2,1,3], k = 3
# Output: true


# Ex 6:
# Input: root = [0,-1,2,-3,null,null,4] , k = -4
# Output: true  -1,2,-3,null,null,4]


# Ex 7:
# Input: root = [1] , k = 2
# Output: false

# Ex 8:
# Input: root = [2,null,3], k = 6
# Output: false

# Unintentional Cases:
# Consider nodes that are NULL
# When finding the sum, the elements don't need to match


# Thought/Pseudo:
# Using BFS, fill up the seen list whlie you traverse the tree (Use queue) #FIFO
# After you have the seen list, utlized the same two sum and find the sum of the target.
# Will need to iterate through twice
# Return a boolean if the target is met


# Code:
def findTarget(root, k):
    # head = root  # The starting Tree Node
    seen = [
        root
    ]  # can put a here set instead of list because BST unique non duplicated values. Prevent cycles
    queue = [root]

    # Use a while loop to traverse the tree until all nodes are none
    while queue:
        node = queue.pop(0)
        if node.left and node.left not in seen:
            seen.append(node.left)  # use add method if using a set()
            queue.append(node.left)
        if node.right and node.right not in seen:
            seen.append(node.right)
            queue.append(node.right)

    seen_lst = list(set(seen))

    # seen_lst_2 = seen_lst[1:]
    # print(seen_lst_2)

    # for num1, num2 in zip(seen_lst, seen_lst_2):
    #     if num1.val + num2.val == k:
    #         return True
    # return False

    if len(seen_lst) == 1:
        return False

    for i, num in enumerate(seen_lst):
        for indx, nums in enumerate(seen_lst):
            if num.val + nums.val == k and i != indx:
                return True
    return False


print(findTarget([5, 3, 6, 2, 4, None, 7], 6))

# Runtime: 1316 ms, faster than 5.10% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 16.7 MB, less than 70.87% of Python3 online submissions for Two Sum IV - Input is a BST.
