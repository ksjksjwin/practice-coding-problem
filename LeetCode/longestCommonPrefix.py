'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

Copyright © 2020 LeetCode

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        min_len_str = min(strs, key=len)

        for i, ch in enumerate(min_len_str):
            for other in strs:
                if other[i] != ch:
                    return min_len_str[:i]

        return min_len_str
