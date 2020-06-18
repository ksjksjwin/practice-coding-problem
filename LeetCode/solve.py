'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Copyright © 2020 LeetCode

'''
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        Solve by BFS
        '''
        #check if board is empty.
        if not board:
            return

        row, col = len(board), len(board[0])

        if row <=2 or col <=2:
            return

        queue = deque()

        #put all the boarder value to the queue. (In tuple format)

        #boarder for row
        for r in range(row):
            queue.append((r, 0))
            queue.append((r, col-1))
        #boarder for col
        for c in range(col):
            queue.append((0, c))
            queue.append((row-1, c))

        #loop until queue is not empty
        while queue:
            r, c = queue.popleft()

            #pass the value if and only if value is valid between row and column.
            if 0 <= r < row and 0 <= c < col and board[r][c] == 'O':
                #modify the vale "O" to "N"
                board[r][c] = "N"
                #Append the surrounding cells of "O" to queue --> nearest surrounding cells will keep added to the queue and process by order --> BFS
                queue.append((r, c+1))
                queue.append((r, c-1))
                queue.append((r-1, c))
                queue.append((r+1, c))

        #Once loop is over, now we replace all the "O" to "X" and "N" to "O"
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "N":
                    board[r][c] = "O"
