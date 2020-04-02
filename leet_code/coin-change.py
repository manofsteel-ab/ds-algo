"""
You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""

class Solution:
    def coinChange(self, coins, amount):
        if not amount:
            return 0
        target = amount+1
        dp = [float(inf)]*(target+1)
        dp[0] = 0
        for amount in range(1,target):
            for coin in coins:
                if coin<=amount:
                    needed = dp[amount-coin]
                    if needed!=inf and needed+1<dp[amount]:
                        dp[amount] = needed+1
        if dp[amount]!=inf:
            return dp[amount]
        return -1
