'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Copyright © 2020 LeetCode

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #Initialize with Null value for first element of reverse
        prev = None

        while head:
            curr = head #copy head to 'curr'
            head = head.next #move 'head'
            curr.next = prev #reverse occur with 'curr'
            prev = curr #copy 'curr' to prev to keep save the reversed Linked List

        return prev
