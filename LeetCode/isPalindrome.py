'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

Copyright © 2020 LeetCode

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        1. Remove all white spaces in s.
        2. find a middle index.
        3. Compare starting from the beginning and end to the middle.
        4. If palindrome, return True. If not, return False.
        '''
        #s.replace(" ", "")

        #used join(), isalnum(), lower() method
        s = ''.join(char for char in s if char.isalnum()).lower()
        middle = len(s) // 2


        for i in range(middle):
            if s[i] != s[-1-i]:
                return False

        return True
