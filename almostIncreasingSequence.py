'''
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
[input] array.integer sequence
[output] boolean

Copyright to © 2020 BrainFights Inc. All rights reserved
'''
#create new function to find a bad number index
def find_bad_number_index(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    index = find_bad_number_index(sequence)
    if index == -1:
        return True #List is increasing
    elif find_bad_number_index(sequence[index-1:index] + sequence[index+1:]) == -1:
        return True  #Deleting earlier element makes increasing
    elif find_bad_number_index(sequence[index:index+1] + sequence[index+2:]) == -1:
        return True #Deleting later element makes increasing
    else:
        return False #If all above case failed, it it not increasing list
