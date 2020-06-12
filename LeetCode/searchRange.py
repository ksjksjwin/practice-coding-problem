'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Copyright © 2020 LeetCode

'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        res[0] = self.findLeftIndex(nums,target)
        res[1] = self.findRightIndex(nums,target)

        return res

    def findLeftIndex(self,nums,target):
        index = -1
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start+end) // 2

            if nums[mid] == target:
                index = mid

            if nums[mid] >= target:
                end = mid-1
            else:
                start = mid+1

        return index

    def findRightIndex(self,nums,target):
        index = -1
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start+end) // 2

            if nums[mid] == target:
                index = mid

            if nums[mid] <= target:
                start = mid+1
            else:
                end = mid-1

        return index
