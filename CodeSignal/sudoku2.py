'''
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;

For

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
sudoku2(grid) = false.

The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''
def sudoku2(grid):
    #check validation for each row
        for row in range(len(grid)):
            if ValidRow(grid,row) == False:
                    return False

        #check validation for each column
        for col in range(len(grid)):
            if ValidCol(grid,col) == False:
                return False

        #check validation for 3X3 each box
        for row in range(0,len(grid),3):
            for col in range(0,len(grid),3):
                if ValidBox(grid, row, col) == False:
                    return False

        return True

def ValidRow(grid, row):
    check_list = []
    for i in range(len(grid)):
        if grid[row][i] in check_list:
            return False
        elif grid[row][i] != '.':
            check_list.append(grid[row][i])
    return True

def ValidCol(grid, col):
        check_list = []
        for i in range(len(grid)):
            if grid[i][col] in check_list:
                return False
            elif grid[i][col] != '.':
                check_list.append(grid[i][col])
        return True

def ValidBox(grid, startRow, startCol):
        check_list = []
        for row in range(3):
            for col in range(3):
                box_val = grid[startRow + row][startCol + col]
                if box_val in check_list:
                    return False
                elif box_val != '.':
                    check_list.append(box_val)
        return True
