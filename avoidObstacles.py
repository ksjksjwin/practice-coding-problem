'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

Copyright to © 2020 BrainFights Inc. All rights reserved
'''

def avoidObstacles(inputArray):

    for i in range(1,max(inputArray)):
        ans = all([x%i for x in inputArray])

        if ans:
            return i

    return max(inputArray)+1
