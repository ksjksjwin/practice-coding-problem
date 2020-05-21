"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.

Copyright to © 2020 BrainFights Inc. All rights reserved

"""

def evenDigitsOnly(n):
    for char in str(n):
        if int(char) % 2 != 0:
            return False
    return True
