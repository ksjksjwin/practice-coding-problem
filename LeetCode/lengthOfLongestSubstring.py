'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer1 = 0
        pointer2 = 0
        maxlen = 0
        tempDict = dict()

        while pointer2 < len(s):
            if s[pointer2] not in tempDict:
                tempDict[s[pointer2]] = 1
                maxlen = max(maxlen, len(tempDict))
                pointer2 += 1
            else:
                tempDict.pop(s[pointer1])
                pointer1 += 1

        return maxlen
