'''
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def validTime(time):
    if (0<= int(time[:2]) <= 23) and (0<= int(time[3:]) <= 59):
        return True
    return False
