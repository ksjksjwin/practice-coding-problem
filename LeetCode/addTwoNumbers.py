'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Copyright © 2020 LeetCode

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = curr = ListNode(0)
        carryOver = 0

        while l1 or l2 or carryOver:
            if l1:
                carryOver += l1.val
                l1 = l1.next

            if l2:
                carryOver += l2.val
                l2 = l2.next

            curr.next = ListNode(carryOver % 10)
            carryOver //= 10
            curr = curr.next

        return res.next
