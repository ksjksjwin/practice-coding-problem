'''
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

Example

For cell = "a1", the output should be
chessKnight(cell) = 2.

For cell = "c2", the output should be
chessKnight(cell) = 6.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''
def chessKnight(cell):
    valid_count = 0

    #All possible moves for knight
    dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    #For each moves of knight, check if valid
    for x, y in dirs:
        if (97 <= ord(cell[0]) + x <= 104) and (1 <= int(cell[1]) + y <= 8):
            valid_count += 1

    return valid_count
