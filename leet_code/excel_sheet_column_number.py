"""
Given a column title as appear in an Excel sheet, return its corresponding
column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
"""


class Solution:
    def _ascii(self, char):
        return ord(char) - 64

    def titleToNumber(self, s: str) -> int:
        str_sz = len(s)
        column_value = 0
        for i in range(0, str_sz):
            column_value = column_value * 26 + self._ascii(s[i])
        return column_value
