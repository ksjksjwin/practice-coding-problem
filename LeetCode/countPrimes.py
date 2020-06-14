'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Copyright © 2020 LeetCode

'''
class Solution:
    def countPrimes(self, n: int) -> int:
        #Creat list of True up to n.
        sieve = [True] * (n)
        #find square root of n.
        sqrtN = int(n ** 0.5)

        for i in range(2, sqrtN+1):
            if sieve[i] == True:
                #change any number that is divisible by prime, we change to False
                for j in range(2*i, n, i):
                    sieve[j] = False

        #list comprehension to find primList (Where it still hold True value)
        primeList = [i for i in range(2,n) if sieve[i] == True]

        return len(primeList)
