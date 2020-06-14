'''
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false

Copyright © 2020 LeetCode

'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #without using loop or recursion
        return n > 0 and 1162261467 % n == 0

        '''
        #With a loop
        for i in range(20):
        #max loop is 31 since max int is 2**31-1 and largest n for power of 3 is 19. 3^19 = 1162261467
            if 3**i == n:
                return True
        return False
        '''
