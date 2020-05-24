'''
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''
def arrayMaxConsecutiveSum(inputArray, k):
    #check prev_sum and current sum
    #compare max_sum with prev_sum and return max

    max_sum = sum(inputArray[:k])

    prev_sum = max_sum

    for i in range(k,len(inputArray)):
        prev_sum = prev_sum - inputArray[i-k] + inputArray[i]
        max_sum = max(max_sum,prev_sum)

    return max_sum
