'''

Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def circleOfNumbers(n, firstNumber):
    half_n = n // 2
    opp_num = firstNumber

    if opp_num < half_n:
        opp_num += half_n
    else:
        opp_num -= half_n

    return opp_num
