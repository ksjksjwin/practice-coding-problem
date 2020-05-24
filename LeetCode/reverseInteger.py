'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Copyright © 2020 LeetCode

'''
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        res = 0

        for i in range(-1,-len(x)-1,-1):
            if x[i] == '-':
                res *= -1
            else:
                res = res*10 + int(x[i])

        if (res < -(2**31)) or (res > (2**31)-1):
            return 0

        return res
