'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Copyright © 2020 LeetCode

'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start = 0 #start index for zeros
        end = len(nums)-1 #end index for twos
        currIndex = 0

        if (len(nums) == 0) and (len(nums) == 1):
            return

        while(currIndex <= end):
            if nums[currIndex] == 0:
                nums[currIndex] = nums[start]
                nums[start] = 0
                currIndex += 1
                start += 1
                #Here we only swap with 1s only. two will go to the end while searching.

            elif nums[currIndex] == 2:
                nums[currIndex] = nums[end]
                nums[end] = 2
                end -= 1
                #No currIndex++, because we do not know what value came from the end. could be 0,1,2

            else:
                currIndex += 1
