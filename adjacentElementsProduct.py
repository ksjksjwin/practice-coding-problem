'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

[input] array.integer inputArray
An array of integers containing at least two elements.

[output] integer
The largest product of adjacent elements.

Problem from CodeSignal.
Copyright to © 2020 BrainFights Inc. All rights reserved
'''
def adjacentElementsProduct(inputArray):
    max_prod_val = -1000000

    for i in range(len(inputArray)-1):
        if inputArray[i] * inputArray[i+1] > max_prod_val:
            max_prod_val = inputArray[i] * inputArray[i+1]

    return max_prod_val
