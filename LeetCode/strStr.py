'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Copyright © 2020 LeetCode

'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        1. First return False if needle not in haystack
        2. use python .index() method to find a first occurrence of a needle in haystack
        '''
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
