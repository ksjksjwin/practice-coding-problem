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
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hashtable = dict()

        for elem in nums:
            if elem not in hashtable.keys():
                hashtable[elem] = 1
            else:
                hashtable[elem] += 1

        for elem in nums:
            if hashtable[elem] == 1:
                return elem

        '''
        for elem in nums:
            if nums.count(elem) > 1:
                continue
            else:
                return elem
        '''
