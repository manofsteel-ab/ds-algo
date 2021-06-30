"""
this is core knapsack algorithm implementation
Problem statement
Given two array, weights[] and values[] which represent weight and values of n items and also given
W which represent knapsack capacity. Find out maximum value subset of values, such that total weight of subset is
lest or equal to W. We can not break item.So Either pic item or don't pick.

"""

"""
this is core knapsack algorithm implementation
Problem statement
Given two array, weights[] and values[] which represent weight and values of n items and also given
W which represent knapsack capacity. Find out maximum value subset of values, such that total weight of subset is
lest or equal to W. We can not break item.So Either pic item or don't pick.

"""


class KnapSack:

    def __init__(self):
        pass

    @classmethod
    def dp_knapsack(cls, weights, values, n, w):
        """
           Time O(n*w) space O(w,n)
           dp[i][j] max value for j capacity using i items
        """
        dp = [[0 for i in range(w+1)] for j in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, w+1):
                if weights[i-1] > w:  # we are not considering ith item
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]])
        return dp[n][w]

    @classmethod
    def dp_knapsack_2(cls, weights, values, n, W):
        """
           Time O(n*w) space O(w)
           dp[w] - max value for capacity w
        """
        dp = [0 for x in range(W+1)]

        for i in range(n):
            for w in range(W, 0, -1):
                if weights[i] <= w:
                    dp[w] = max(dp[w], dp[w-weights[i]+values[i]])
        return dp[w]


obj = KnapSack()

# Driver Code

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(obj.dp_knapsack(wt, val, n, W))
