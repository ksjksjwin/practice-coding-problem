'''
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".

Copyright to © 2020 BrainFights Inc. All rights reserved

'''
def lineEncoding(s):

    res = ''
    count = 1

    for i in range(len(s)-1):

        #check for beginning to right before last element
        if s[i] == s[i+1]:
            count += 1
        elif (s[i] != s[i+1]) and count >= 2:
            res += str(count) + s[i]
            count = 1
        elif (s[i] != s[i+1]):
            res += s[i]
            count = 1

        #check for the last element
        if ((i+1) == len(s)-1) and (s[i] != s[i+1]):
            res += s[i+1]

        elif ((i+1) == len(s)-1) and (s[i] == s[i+1]):
            res += str(count) + s[i+1]

    return res
