"""
Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:

    def _generateParenthisis(self, open_cnt, close_cnt, par_str, results, n):
        if open_cnt == 0 and close_cnt == 0:
            results.append(par_str)
            return
        if open_cnt > 0:
            self._generateParenthisis(open_cnt - 1, close_cnt + 1,
                                      par_str + "(", results, n)
        if close_cnt > 0:
            self._generateParenthisis(open_cnt, close_cnt - 1, par_str + ")",
                                      results, n)

    def generateParenthesis(self, n: int):
        valid_parenthesis = []
        self._generateParenthisis(n, 0, "", valid_parenthesis, n)
        return valid_parenthesis
