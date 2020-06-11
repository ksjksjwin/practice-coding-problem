'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

Copyright © 2020 LeetCode

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Check two cases for if string is odd or even length.
        '''
        left = 0
        right = 0
        longestPal = 0

        for i in range(len(s)):
            curLengthPal, l, r = self.longestAtIndex(s, i, i)
            if curLengthPal > longestPal:
                longestPal = curLengthPal
                left = l
                right = r

            curLengthPal, l, r = self.longestAtIndex(s, i, i+1)
            if curLengthPal > longestPal:
                longestPal = curLengthPal
                left = l
                right = r

        return s[left:right+1]

    #helper function
    def longestAtIndex(self, s, l, r):
        while (l >= 0 and r < len(s)) and (s[l] == s[r]):
            l -= 1
            r += 1
        l += 1
        r -= 1

        return (r-l+1, l, r)
