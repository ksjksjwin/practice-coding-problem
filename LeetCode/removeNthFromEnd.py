'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Copyright © 2020 LeetCode

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #Two-pass algorithm
        dummy, dummy1= ListNode(0), ListNode(0)
        dummy.next, dummy1 = head, dummy
        list_len = 0

        while head:
            list_len += 1
            head = head.next

        while list_len - n > 0:
            list_len -= 1
            dummy = dummy.next

        dummy.next = dummy.next.next

        return dummy1.next
