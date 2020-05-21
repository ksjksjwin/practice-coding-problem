'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

[input] array.integer a
If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

[output] array.integer
Sorted array a with all the trees untouched.

Copyright to © 2020 BrainFights Inc. All rights reserved
'''

def sortByHeight(a):
    index_list = []
    height_list = []

    for i in range(len(a)):
        if a[i] == -1:
            continue
        else:
            index_list.append(i)
            height_list.append(a[i])

    height_list.sort()
    i = 0

    for index in index_list:
        a[index] = height_list[i]
        i += 1

    return a
