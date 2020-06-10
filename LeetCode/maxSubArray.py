'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Copyright © 2020 LeetCode

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maxSum = float('-inf')
        maxAll = float('-inf')

        for i in range(len(nums)):
            maxSum = max(maxSum+nums[i], nums[i])
            maxAll = max(maxSum, maxAll)

        return maxAll
