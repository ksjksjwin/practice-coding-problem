'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Copyright © 2020 LeetCode

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Using bit manipulation
        res = len(nums)

        for i, num in enumerate(nums):
            res ^= i^num

        return res

        '''
        #Brute force to find the sol. --> Still O(1) space and O(N) time complexity
        res = 0

        for i in range(2**31-1):
            if res in nums:
                res += 1
            else:
                return res
        '''
