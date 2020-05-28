'''
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''
def digitsProduct(product):
    for i in range(1,10000):
        number = str(i)
        total = 1

        for char in number:
            total *= int(char)

        if total == product:
            return i

    #if not found return -1
    return -1
