'''
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

Copyright to © 2020 BrainFights Inc. All rights reserved
'''

def alphabeticShift(inputString):

    ans_list = []

    for i in range(len(inputString)):

        if ord(inputString[i]) == 122:
            ans_list.append('a')
            continue

        ans_list.append(chr(ord(inputString[i]) + 1))

    return ''.join(ans_list)
