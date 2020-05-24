'''
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
differentSymbolsNaive(s) = 3.

There are 3 different characters a, b and c.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''
def differentSymbolsNaive(s):
    set_tmp = set()
    count = 0

    for char in s:
        if char in set_tmp:
            continue
        else:
            set_tmp.add(char)
            count += 1

    return count
