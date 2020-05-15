class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            isNeg = True
        else:
            isNeg = False

        x = abs(x)
        ans = 0
        while x > 0:
            rem = x % 10
            ans = ans * 10 + rem
            x = x // 10
        if isNeg:
            ans = ans * -1
        if ans >= 2147483647 or ans <= -2147483648:
            return 0
        else:
            return ans
