'''
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

[input] array.string inputArray
[output] array.string

Copyright to © 2020 BrainFights Inc. All rights reserved
'''

def allLongestStrings(inputArray):
    longest_list = []
    max_len = 0

    for i in range(len(inputArray)):
        if len(inputArray[i]) > max_len:
            max_len = len(inputArray[i])

    for word in inputArray:
        if len(word) == max_len:
            longest_list.append(word)

    return longest_list
