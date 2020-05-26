'''
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
isMAC48Address(inputString) = false.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def isMAC48Address(inputString):
    if '-' not in inputString:
        return False

    splitData = inputString.split('-')

    if len(splitData) != 6:
        return False

    for data in splitData:
        if len(data) != 2:
            return False

        if not ((ord('0') <= ord(data[0]) <= ord('9')) or (ord('A') <= ord(data[0]) <= ord('F'))):
            return False

        if not ((ord('0') <= ord(data[1]) <= ord('9')) or (ord('A') <= ord(data[1]) <= ord('F'))):
            return False

        else:
            continue

    return True
