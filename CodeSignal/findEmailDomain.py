'''
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.

Example

For address = "prettyandsimple@example.com", the output should be
findEmailDomain(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should be
findEmailDomain(address) = "codesignal.com".

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def findEmailDomain(address):
    domain_part = []

    for i in range(-1,-len(address)-1,-1):
        if address[i] != '@':
            domain_part.insert(0,address[i])
        else:
            break
    return "".join(domain_part)
