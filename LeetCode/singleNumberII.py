'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

Copyright © 2020 LeetCode

'''
#from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            count = 0
            for n in nums:
                count += (n >> i) & 1
            rem = count % 3
            if i == 31 and rem:  # must handle the negative case
                res -= 1 << 31
            else:
                res |= rem << i

        return res
        '''
        #Use extra memory of dict()
        numsDict = defaultdict(int)

        for num in nums:
            numsDict[num] += 1

        for key in numsDict:
            if numsDict[key] == 1:
                return key
        '''
