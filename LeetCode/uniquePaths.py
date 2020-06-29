'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?



Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

Copyright © 2020 LeetCode

'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for i in range(m)] for j in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[n-1][m-1]
