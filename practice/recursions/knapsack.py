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
    def recursive_knapsack(cls, weights, values, n, w):
        if n == 0 or w == 0:
            return 0

        # if nth item is > w
        if weights[n-1] > w:
            return cls.recursive_knapsack(weights, values, n-1, w)
        else:
            return max(
                values[n-1] + cls.recursive_knapsack(weights, values, n-1, w-weights[n-1]),
                cls.recursive_knapsack(weights, values, n - 1, w)
            )


obj = KnapSack()

# Driver Code

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(obj.recursive_knapsack(wt, val, n, W))
