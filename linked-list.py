# Q1: Reverse Linked List (206):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        curr_node = head
        prev_node = None
        while head is not None:
            next_node = curr_node.next_node
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node


# Test Case:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# =================================
# Q2: (876)
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.

# Special Cases:

# None:
# I: []
# O: None

# One:
# I: [1]
# O: 1

# Negative numbers:
# I: [-1,-2,-3]
# O: None -- Expected integers between 1-100, no negatives

# Won't take into account non integer types (ie string, float, etc)

# Thought:
# Take the length of the list and determine whether even or odd
# Traverse through the linked list and count
# If count is Odd, then divide the length by two and whatever that whole division is the index at which the middle is located. But because this isn't an array, then traverse through list until you find the result, then add 1

# If count is Even, divide length by half and take the result at that index. But because this isn't an array, then traverse through list until you find the result, then add 1

# Questions:
# Can you do len on linked list? - None, need to initiate an counter
# But can turn into an Array, as will see in the alternative solution methods below


# Code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         len_count = 0

#         while head is not None:
#             current_node = head
#             next_node = head.next
#             len_count += 1

#         middle_point = len_count / 2   #Note: "//" return float, not whole

#         final_point = 0

#         if len_count%2 == 1:  #if odd
#             while final_point != middle_point + 1:
#                 current_node = head
#                 next_node = head.next
#                 final_point += 1

#         return next_node


#         if len_count%2 == 0:  #if even
#             while final_point != middle_point + 1:
#                 current_node = head
#                 next_node = head.next
#                 final_point += 1

#         return next_node

# ===================
# Output to Array
class Solution(object):
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) / 2]


# Time Complexity: O(N)O(N), where NN is the number of nodes in the given list.

# Space Complexity: O(N)O(N), the space used by A.


# ==================
# Fast and Slow Pointer


class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Time Complexity: O(N)O(N), where NN is the number of nodes in the given list.

# Space Complexity: O(1)O(1), the space used by slow and fast.


# =================================
# Q3: (234) Palindrome Linked List
# Given a singly linked list, determine if it is a palindrome.

# Test Cases:
# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Thoughts:
# Traverse through the linked list and append it to a new array
# Then reverse the array and see if it matches the new array

# Pseudocode:
# Create a new_array
# Traverse through the list and add those nodes to the new array
# Create a reverse array list
# Compare the new array to the reversed array
# If the same, return True
# Else, return False


# Code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        new_array = []
        curr_node = head

        while curr_node is not None:
            new_array.append(curr_node)  # Append the starting head to the array
            next_node = curr_node.next  # next node
            curr_node = next_node  # New head
            new_array.append(curr_node)  # Append the next node (new head) to the array

        reverse_array = new_array[::-1]

        if new_array == reverse_array:
            return True
        else:
            return False


# NOTE: This solution above DOES NOT pass because you are passing in the class ListNode itself as the head.
# So the stout:
# [ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}, ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}, ListNode{val: 2, next: ListNode{val: 1, next: None}}, ListNode{val: 1, next: None}]

# [ListNode{val: 1, next: None}, ListNode{val: 2, next: ListNode{val: 1, next: None}}, ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}, ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}]

# =======================
# NOTE: Thus, you need to add .val attribute from the ListNode class. (See below)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        new_array = []
        curr_node = head

        while curr_node != None:
            new_array.append(curr_node.val)  # Append the starting head to the array
            next_node = curr_node.next  # next node
            curr_node = next_node  # New head
            # new_array.append(curr_node)  # Append the next node (new head) to the array

        reverse_array = new_array[::-1]

        print(new_array)
        print()
        print(reverse_array)

        if new_array == reverse_array:
            return True
        else:
            return False


# Stdout:
# [1, 2, 2, 1]

# [1, 2, 2, 1]

# 80ms, so slow. Runtime of O(n)
# Time complexity of Python reverse is O(n) or linear time

# Next challenge, is slow and fast pointer....to implement here

# ===============================================================
# Q4: Merge Two Sorted Lists (21)

# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists.

# Test Cases:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: l1 = [], l2 = []
# Output: []

# Example 3:

# Input: l1 = [], l2 = [0]
# Output: [0]

# Special Cases: None, One, Many
# See test cases above

# Thought/Pseudo:
# Know the list is already sorted! Both of them
# Create list_one and traverse through the linked list and add to this array
# Create list_two and traverse through the linked list and add to this array
# Create an empty new list, hold the final sorted values
# Concatenate the two lists together into a new list
# Sort the new list together.
# use the sorted or sort method Python
# Sorting algorithmn (Merge sort??)

# Questions:
# Can we use the Python sort method?
# Are the linked list the same number of items or length? - NO, as seen in test cases


# Code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lst_1 = []  # Start with the head added to lst
        lst_2 = []

        curr_node_1 = l1
        curr_node_2 = l2

        while curr_node_1 != None:
            lst_1.append(curr_node_1)
            next_node = l1.next  # next node after head
            curr_node_1 = next_node  # update the head

        while curr_node_2 != None:
            lst_2.append(curr_node_2)
            next_node = l2.next
            curr_node_2 = next_node

        lst_1_and_2 = lst_1 + lst_2  # concatenate the two lists together

        return sorted(lst_1_and_2)  # return sorted list

