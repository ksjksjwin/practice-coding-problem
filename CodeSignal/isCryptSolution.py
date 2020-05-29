'''
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.

Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

Example

For crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
the output should be
isCryptSolution(crypt, solution) = true.

When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

For crypt = ["TEN", "TWO", "ONE"] and

solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
the output should be
isCryptSolution(crypt, solution) = false.

Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, meaning that this is not a valid solution.

Copyright to © 2020 BrainFights Inc. All rights reserved

'''
def isCryptSolution(crypt, solution):
    '''
    convert the solution to dict
    find each character in the solution and calculate the value
    return if it is valud calculation, false otherwise
    '''

    solution_dict = dict(solution)
    word1_number = ''
    word2_number = ''
    word3_number = ''

    #First word
    for char in crypt[0]:
        word1_number += solution_dict.get(char)
    if word1_number[0] == '0' and len(word1_number) != 1:
        return False
    word1_number = int(word1_number)

    #Second word
    for char in crypt[1]:
        word2_number += solution_dict.get(char)
    if word2_number[0] == '0' and len(word2_number) != 1:
        return False
    word2_number = int(word2_number)

    #Third word
    for char in crypt[2]:
        word3_number += solution_dict.get(char)
    if word3_number[0] == '0' and len(word3_number) != 1:
        return False
    word3_number = int(word3_number)

    return (word1_number + word2_number) == word3_number
