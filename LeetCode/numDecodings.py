'''
91. Decode Ways
Medium

2519

2724

Add to List

Share
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Copyright © 2020 LeetCode

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        #initialize memo to hold the data to avoid redundant process
        memo = [None for _ in range(len(s)+1)]
        #call helper function
        return self.helper_dp(s, len(s), memo)

    def helper_dp(self, s, n, memo):
        #base case
        if n == 0:
            return 1

        #for each recursive call, we set and check the start index.
        startIndex = len(s) - n

        #for any case when start index is 0 --> '006' --> can't convert to letters.
        if s[startIndex] == '0':
            return 0

        #if we already have data in memo, we skip the recursive calls and return the data.
        if memo[n] != None:
            return memo[n]

        #recursive calls for 2 cases. "12" --> we can convert to either "1 2" or "12"
        result = self.helper_dp(s, n-1, memo)
        if n >=2 and int(s[startIndex:startIndex+2]) <= 26:
            result += self.helper_dp(s, n-2, memo)

        #save the result to memo
        memo[n] = result

        return result
