"""
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to
find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""


class Solution:
    def maxProfit(self, prices) -> int:
        sz = len(prices)
        if sz == 0:
            return 0
        start_index = sz - 1
        mx = prices[start_index]
        stack = [None] * sz  # this will store max value on right side
        stack[start_index] = mx
        start_index -= 1
        profit = 0
        while start_index >= 0:
            mx = max(mx, prices[start_index])
            stack[start_index] = mx
            profit = max(profit, stack[start_index] - prices[start_index])
            start_index -= 1
        return profit
