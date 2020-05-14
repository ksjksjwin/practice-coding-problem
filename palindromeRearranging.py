'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
Copyright to © 2020 BrainFights Inc. All rights reserved
'''

def palindromeRearranging(inputString):
    count_list = [0] * 256

    for char in inputString:
        count_list[ord(char)] += 1

    odd_count = 0

    for i in range(len(count_list)):
        if count_list[i] % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return False

    return True
