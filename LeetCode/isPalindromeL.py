'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

Copyright © 2020 LeetCode

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head

        #Find a mid
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #Reverse the second half of the Linked List
        reverse_node = None
        while slow:
            copy_slow_next = slow.next #Keep move the original slow and have copy of it *original slow does not move yet
            slow.next = reverse_node #[reverse] slow next point to the saved 'reverse_node' Linked List`
            reverse_node = slow #[reverse]current position of 'slow' LinkedList
            slow = copy_slow_next  #since we needt to move 'slow' linked list, copy 'copy_slow_next' linked list which is already moved

        #Compare 1st half and 2nd half
        while head and reverse_node:
            if head.val != reverse_node.val:
                return False
            head = head.next
            reverse_node = reverse_node.next

        return True
