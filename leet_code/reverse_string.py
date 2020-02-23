"""
Write a function that reverses a string. The input string is given as an array
 of characters char[].

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        sz = len(s)
        for i in range(0, int(sz/2)):
            s[i], s[sz-i-1] = s[sz-i-1], s[i]
