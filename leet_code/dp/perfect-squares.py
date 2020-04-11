# Lagrange’s Four Square Theorem states that every natural number can be
# written as sum of squares of four non negative integers.

class Solution:
    def numSquares(self, n):
        if n<4:
            return n
        sqr = int(sqrt(n))+1
        pool = {i**2 for i in range(sqr)}
        test = [i**2 for i in range(sqr)]
        for i in test:
            for j in test:
                if n-i-j in pool:
                    return 3 - (i==0) - (j==0)
        return 4
