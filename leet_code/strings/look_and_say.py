"""

The count-and-say sequence is the sequence of integers with the first
five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say
sequence. You can do so recursively, in other words from the previous member
read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
"""


class Solution:

    def _getCountString(self, num: str):
        res = ""
        i = 0
        while i < len(num):
            count = 1
            current_char = num[i]
            j = i + 1
            while j < len(num) and num[i] == num[j]:
                count += 1
                j += 1
            res += str(count) + current_char
            i = j
        return res

    def countAndSay(self, n: int) -> str:
        dp = ["1", "11", "21", "1211", "111221"]

        if n <= 5:
            return dp[n - 1]

        for i in range(5, n):
            last = dp[i - 1]
            dp.append(self._getCountString(last))
        return dp[n - 1]
