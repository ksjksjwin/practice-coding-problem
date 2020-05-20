'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Copyright © 2020 LeetCode

'''

def ValidRow(board, row):
    check_list = []
    for i in range(len(board)):
        if board[row][i] in check_list:
            return False
        elif board[row][i] != '.':
            check_list.append(board[row][i])
    return True

def ValidCol(board, col):
        check_list = []
        for i in range(len(board)):
            if board[i][col] in check_list:
                return False
            elif board[i][col] != '.':
                check_list.append(board[i][col])
        return True

def ValidBox(board, startRow, startCol):
        check_list = []
        for row in range(3):
            for col in range(3):
                box_val = board[startRow + row][startCol + col]
                if box_val in check_list:
                    return False
                elif box_val != '.':
                    check_list.append(box_val)
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check validation for each row
        for row in range(len(board)):
            if ValidRow(board,row) == False:
                    return False

        #check validation for each column
        for col in range(len(board)):
            if ValidCol(board,col) == False:
                return False

        #check validation for 3X3 each box
        for row in range(0,len(board),3):
            for col in range(0,len(board),3):
                if ValidBox(board, row, col) == False:
                    return False

        return True
