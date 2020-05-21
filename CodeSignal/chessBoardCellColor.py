'''
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def chessBoardCellColor(cell1, cell2):

    if (cell1[0] in 'ACEG') and (cell2[0] in 'ACEG') and (int(cell1[1]) % 2 == 1) and (int(cell2[1]) % 2 == 1):
        return True
    elif (cell1[0] in 'BDFH') and (cell2[0] in 'BDFH') and (int(cell1[1]) % 2 == 0) and (int(cell2[1]) % 2 == 0):
        return True
    elif (cell1[0] in 'ACEG') and (cell2[0] in 'BDFH') and (int(cell1[1]) % 2 == 1) and (int(cell2[1]) % 2 == 0):
        return True
    elif (cell1[0] in 'BDFH') and (cell2[0] in 'ACEG') and (int(cell1[1]) % 2 == 1) and (int(cell2[1]) % 2 == 0):
        return True
    elif (cell1[0] in 'ACEG') and (cell2[0] in 'BDFH') and (int(cell1[1]) % 2 == 0) and (int(cell2[1]) % 2 == 1):
        return True
    elif (cell1[0] in 'BDFH') and (cell2[0] in 'BDFH') and (int(cell1[1]) % 2 == 1) and (int(cell2[1]) % 2 == 1):
        return True

    return False
