'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Copyright © 2020 LeetCode

'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_dict = {}
        ans = []

        for num in nums1:
            count_dict[num] = count_dict.get(num, 0) + 1

        for num in nums2:
            if (num in count_dict) and (count_dict[num] > 0):
                ans.append(num)
                count_dict[num] -= 1

        return ans
