"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            ')': '(', '}': '{', ']': '['
        }
        for i in range(0, len(s)):
            if s[i] in mp.values():
                stack.append(s[i])
            elif s[i] in mp.keys() and stack and mp[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False
