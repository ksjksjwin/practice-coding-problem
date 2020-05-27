'''
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def deleteDigit(n):

    #find index that any next number is higher than current number

    n = str(n)
    res = 0

    for i in range(len(n)-1):
        if int(n[i]) < int(n[i+1]):
            res = int(n[:i] + n[i+1:])
            break

    if res == 0:
        res = int(n[:-1])

    return res
