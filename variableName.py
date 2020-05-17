'''
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
For name = "2w2", the output should be
variableName(name) = false.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def variableName(name):
    if name[0].isdigit():
        return False

    for char in name:
       if char == '_':
           continue
       if (char.isalpha() == False) and (char.isdigit() == False):
           return False
    return True
