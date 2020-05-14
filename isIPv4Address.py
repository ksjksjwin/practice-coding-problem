'''
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.

There is no first number.

*IPV4 ADDRESS*
An identification number for devices connected to the internet. An IPv4 addresses written in dotted quad notation consists of four 8-bit integers separated by periods.

In other words, it's a string of four numbers each between 0 and 255 inclusive, with a "." character in between each number. All numbers should be present without leading zeros.

Examples:

192.168.0.1 is a valid IPv4 address
255.255.255.255 is a valid IPv4 address
280.100.92.101 is not a valid IPv4 address because 280 is too large to be an 8-bit integer (the largest 8-bit integer is 255)
255.100.81.160.172 is not a valid IPv4 address because it contains 5 integers instead of 4
1..0.1 is not a valid IPv4 address because it's not properly formatted
17.233.00.131 and 17.233.01.131 are not valid IPv4 addresses because they contain leading zeros

Copyright to © 2020 BrainFights Inc. All rights reserved
'''
def isIPv4Address(inputString):
    number_list = []
    number_str = ''

    number_list = inputString.split('.')
    print(number_list)

    if len(number_list) != 4:
        return False

    for number in number_list:
        if number == '':
            return False
        elif number.isnumeric() == False:
            return False
        elif len(number) > 1 and number[0] == '0':
            return False
        elif int(number) > 255 or int(number) < 0:
            return False

    return True
