'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Copyright © 2020 LeetCode

'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]

            row[0], row[-1] = 1, 1

            for i in range(1,len(row)-1):
                row[i] = triangle[row_num-1][i-1] + triangle[row_num-1][i]

            triangle.append(row)

        return triangle
