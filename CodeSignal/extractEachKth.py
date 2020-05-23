'''
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

Copyright to © 2020 BrainFights Inc. All rights reserved

'''
def extractEachKth(inputArray, k):
    ans = []
    i = 0
    while i < len(inputArray):
        if (i+1) % k != 0:
            ans.append(inputArray[i])
        i += 1
    return ans
