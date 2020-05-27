'''
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".

Copyright to © 2020 BrainFights Inc. All rights reserved

'''

def longestWord(text):
    temp_list = []
    word = ''
    res = ''

    for char in text:
        #add the characters when it is meet special character or space
        if char.isalpha() == False:
            temp_list.append(word)
            word = ''

        #Keep adding the character until it meet special character or space
        if char.isalpha():
            word += char

    #add last word if it does not meet the any special character or space
    temp_list.append(word)

    #find maximum length word
    for i in range(len(temp_list)):
        if len(temp_list[i]) > len(res):
            res = temp_list[i]

    return res
