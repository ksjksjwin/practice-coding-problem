'''
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Copyright © 2020 LeetCode

'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #special case if s is 0.
        if len(s) == 0:
            return True

        pointerS = 0
        pointerT = 0

        #keep loop until "pointerT reach out to end" or "pointerS reach out to the end."
        while (pointerT < len(t)) and (pointerS != len(s)):
            if s[pointerS] == t[pointerT]:
                pointerS += 1
                pointerT += 1
            else:
                pointerT += 1

        if pointerS == len(s):
            return True

        return False
