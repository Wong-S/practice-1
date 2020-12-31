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

#=================================
# Q2: (876) 
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

#Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.

#Special Cases:

    #None:
        I: []
        O: None

    #One:
        I: [1]
        O: 1

    #Negative numbers:
        I: [-1,-2,-3]
        O: None -- Expected integers between 1-100, no negatives

    #Won't take into account non integer types (ie string, float, etc)

#Thought:
    #Take the length of the list and determine whether even or odd
        #Traverse through the linked list and count
    #If count is Odd, then divide the length by two and whatever that whole division is the index at which the middle is located. But because this isn't an array, then traverse through list until you find the result, then add 1

    #If count is Even, divide length by half and take the result at that index. But because this isn't an array, then traverse through list until you find the result, then add 1

#Questions:
    #Can you do len on linked list? - None, need to initiate an counter
            #But can turn into an Array, as will see in the alternative solution methods below


#Code:
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
            
#===================
#Output to Array
# class Solution(object):
#     def middleNode(self, head):
#         A = [head]
#         while A[-1].next:
#             A.append(A[-1].next)
#         return A[len(A) / 2]

#Time Complexity: O(N)O(N), where NN is the number of nodes in the given list.

# Space Complexity: O(N)O(N), the space used by A.


#==================
#Fast and Slow Pointer

#class Solution(object):
    # def middleNode(self, head):
    #     slow = fast = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow

#Time Complexity: O(N)O(N), where NN is the number of nodes in the given list.

#Space Complexity: O(1)O(1), the space used by slow and fast.


