'''
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
longestDigitsPrefix(inputString) = "123".

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def longestDigitsPrefix(inputString):
    longestDigits = ""
    for char in inputString:
        if char.isdigit():
            longestDigits += char
        else:
            break
    return longestDigits
