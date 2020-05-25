'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Copyright © 2020 LeetCode

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_dict_s = dict()
        temp_dict_t = dict()

        for char in s:
            temp_dict_s[char] = temp_dict_s.get(char,0)+1

        for char in t:
            temp_dict_t[char] = temp_dict_t.get(char,0)+1

        if temp_dict_s == temp_dict_t:
            return True

        return False
