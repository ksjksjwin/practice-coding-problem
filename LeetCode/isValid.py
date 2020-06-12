'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

Copyright © 2020 LeetCode

'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            #check if current index of s is open brackets.
            if s[i] in '([{':
                stack.append(s[i])
            #pop and check with current closed bracket.
            else:
                #return false since we have no more open brackets.
                if len(stack) == 0:
                    return False
                op = stack.pop()
                cl = s[i]

                if not self.isParenSameType(op,cl):
                    return False

        return len(stack) == 0

    #helper function to check open and closed bracket
    def isParenSameType(self,op,cl):
        if op == '(' and cl == ')':
            return True
        elif op == '{' and cl == '}':
            return True
        elif op == '[' and cl == ']':
            return True
        else:
            return False
