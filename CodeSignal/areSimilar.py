'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
Copyright to © 2020 BrainFights Inc. All rights reserved
'''

def areSimilar(a, b):
    if a == b:
        return True

    temp_list1 = []
    temp_list2 = []

    for i in range(len(a)):
        if a[i] != b[i]:
            temp_list1.append(a[i])
            temp_list2.append(b[i])

    temp_list2.reverse()

    print(temp_list1)
    print(temp_list2)

    if (len(temp_list1) == 2) and (temp_list1 == temp_list2):
        return True

    return False
