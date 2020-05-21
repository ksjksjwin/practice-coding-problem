'''
Given the string, check if it is a palindrome.

[input] string inputString
A non-empty string consisting of lowercase characters.

[output] boolean
true if inputString is a palindrome, false otherwise.
'''
def checkPalindrome(inputString):
    pivot = len(inputString) // 2

    for i in range(pivot):
        if inputString[i] == inputString[-1-i]:
            continue
        else:
            return False

    return True
