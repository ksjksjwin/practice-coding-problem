'''
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def differentSquares(matrix):
    res_set = set()
    temp_str = ''

    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            temp_str = str(matrix[i][j]) + str(matrix[i][j+1]) + str(matrix[i+1][j]) + str(matrix[i+1][j+1])
            res_set.add(temp_str)

    return len(res_set)
