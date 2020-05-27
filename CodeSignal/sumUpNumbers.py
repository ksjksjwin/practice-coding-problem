'''
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
sumUpNumbers(inputString) = 14.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''
def sumUpNumbers(inputString):
    number = ''
    res = 0
    for char in inputString:
        #add number to string only if number
        if char.isdigit():
            number += char

        #if the char is not a number and length is not zero, add the number to res
        if char.isdigit() == False and len(number) != 0:
           res += int(number)
           number = ''

    #add the last number that didn't hit any alphabet or special character if number saved
    if len(number) != 0:
        res += int(number)

    return res
