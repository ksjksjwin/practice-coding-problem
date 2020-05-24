'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

Copyright © 2020 LeetCode

'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp_dict = dict()

        for char in s:
            temp_dict[char] = temp_dict.get(char,0) + 1

        for i in range(len(s)):
            if temp_dict[s[i]] == 1:
                return i
        return -1
