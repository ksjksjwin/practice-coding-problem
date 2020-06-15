'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

Copyright © 2020 LeetCode

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        #Solution without using extra memory of left and right product list
        '''
        lenList = len(nums)
        resList = [0]*lenList

        #update resList with left production.
        resList[0] = 1
        for i in range(1,lenList):
            resList[i] = resList[i-1] * nums[i-1]

        rightProd = 1
        for i in reversed(range(lenList)):
            resList[i] = resList[i] * rightProd
            rightProd *= nums[i]

        return resList

        '''
        #Soultion using extra n space for left and right list

        lenList = len(nums)
        leftList, rightList, resList = [0]*lenList, [0]*lenList, [0]*lenList

        #left list for product
        leftList[0] = 1
        for i in range(1,lenList):
            leftList[i] = leftList[i-1] * nums[i-1]

        #right list for product
        rightList[-1] = 1 #rightList[length-1] = 1
        for i in range(-2,-lenList-1,-1): #for i in reversed(range(lenList-1))
            rightList[i] = rightList[i+1] * nums[i+1]

        for i in range(lenList):
            resList[i] = leftList[i] * rightList[i]

        return resList
        '''
