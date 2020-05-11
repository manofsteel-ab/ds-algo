class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        total_profit = 0
        prices_len = len(prices)

        if prices_len<2:
            return 0

        left_dp = [0]*prices_len
        right_dp = [0]*prices_len

        # left dp
        min_element = prices[0]
        for i in range(1, prices_len):
            if prices[i]>min_element:
                left_dp[i] = max(left_dp[i-1],prices[i]-min_element)
            else:
                left_dp[i] = left_dp[i-1]
                min_element = prices[i]
        # right dp
        max_element = prices[-1]
        for i in range(prices_len-2,-1,-1):
            if prices[i]<max_element:
                right_dp[i] = max(right_dp[i+1],max_element - prices[i])
            else:
                left_dp[i] = left_dp[i+1]
                max_element = prices[i]

        total_profit = left_dp[0]
        for i in range(prices_len):
            if i<prices_len-1:
                total_profit = max(total_profit, left_dp[i]+right_dp[i+1])
            else:
                total_profit = max(total_profit, left_dp[i])

        return total_profit
