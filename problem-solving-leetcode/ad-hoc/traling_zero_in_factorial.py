class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        counter = 5
        while n // counter >= 1:
            ans += n // counter
            counter = counter * 5
        return ans

