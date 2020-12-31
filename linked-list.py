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

