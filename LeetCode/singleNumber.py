'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

Copyright © 2020 LeetCode

'''
#from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Using bit manipulation of XOR --> a^0 = a , a^a = 0
        #Space memory(1)

        res = 0

        for num in nums:
            res^=num
        return res

        '''
        #using dict -> space memory(n)
        numDict = defaultdict(int)

        for num in nums:
            numDict[num] += 1

        for key in numDict:
            if numDict[key] == 1:
                return key
        '''
