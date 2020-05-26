'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".

Copyright to © 2020 BrainFights Inc. All rights reserved

'''
def buildPalindrome(st):

    for i in range(len(st)):
        substring = st[i:]

        if isPalindrom(substring):
            nonPalindromString = st[:i]
            return st + nonPalindromString[::-1]


def isPalindrom(st):
    return st == st[::-1]
