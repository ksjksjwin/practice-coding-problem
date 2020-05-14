'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

Copyright to © 2020 BrainFights Inc. All rights reserved
'''

def arrayChange(inputArray):
    step_count = 0

    for i in range(len(inputArray)-1):
        if inputArray[i+1] <= inputArray[i]:
            step_count += (inputArray[i] - inputArray[i+1]) + 1
            inputArray[i+1] = inputArray[i] + 1
    return step_count
