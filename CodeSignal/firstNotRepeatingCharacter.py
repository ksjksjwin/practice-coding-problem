'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def firstNotRepeatingCharacter(s):
    #Linear search algorithm

    if len(s) == 1:
        return s

    temp_set = set()

    for i in range(len(s)-1):
        if (s[i] not in temp_set) and (s[i] not in s[i+1:]):
            return s[i]

        temp_set.add(s[i])

    return '_'

'''
solution using rindex() method

for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'

'''
