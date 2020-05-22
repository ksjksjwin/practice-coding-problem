'''
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

from itertools import permutations
#import permutations function from itertools

def stringsRearrangement(inputArray):
    Allpermutation_tuple = permutations(inputArray)
    #Generate All permutation tuple
    '''
    Example: ('ab', 'bb', 'ba')
             ('ab', 'aa', 'bb')
                    ...
                    ...

    '''

    for permuElement in Allpermutation_tuple:
        ans = True
        #print(permuElement)
        for i in range(len(permuElement)-1):
            if differbyOneChar(permuElement[i], permuElement[i+1]) == False:
                ans = False
                break
                #if any consecutive pair in permuElement is not differ by one characeter, break and check next element in Allpermutation_tuple

        if ans == True:
            return ans
            #After check all element in permuElement and all element is differ by once character in consecutive order, we return true.

    return False
    #After all loop, if none of the permuElement meet the requirement then return False

#Create helper function to compare and find if each element in permuElement is differ by once character.
def differbyOneChar(str1, str2):
    differ_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            differ_count += 1

    if differ_count != 1:
        return False

    return True
