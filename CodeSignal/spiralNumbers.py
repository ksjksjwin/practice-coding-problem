'''
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def spiralNumbers(n):

    #create a N*N matrix
    matrix = [[0] * n for i in range(n)]


    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1

    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            matrix[x][y] = c
            c += 1

    return matrix
