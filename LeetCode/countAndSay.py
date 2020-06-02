'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".

Copyright © 2020 LeetCode

'''
class Solution:
    def countAndSay(self, n: int) -> str:
        #Feed the first stage
        start = '1'

        #Loop through the n-1 since we alraedy feed first stage
        for _ in range(n-1):

            first_char = start[0]
            new_start = ''
            count = 0

            #Loop through all character in previous stage
            for char in start:
                if first_char == char: #if character is same, increase the count
                    count += 1
                else:
                    new_start += str(count)+first_char
                    #if hit other character, update the first_char and count = 1
                    first_char = char
                    count = 1

            new_start += str(count)+first_char #Adding the left count and say
            start = new_start #update the start with a new_start

        return start
