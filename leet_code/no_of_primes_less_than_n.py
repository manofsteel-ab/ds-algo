"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        non_primes = {}
        ans = 1
        i = 3
        while i < n:
            if not non_primes.get(i):
                ans += 1
                non_primes[i] = True
                j = 2 * i
                while j < n:
                    non_primes[j] = True
                    j += i
            i += 2
        return ans


class Solution2:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        else:
            markers = [1]*n
            markers[0] = 0
            markers[1] = 0
            m = 2
            while m*m < n:
                if markers[m] == 1:
                    markers[m*m:n:m] = [0] * (1 + (n-1-m*m)//m)
                    # print(markers)
                m += 1
            return sum(markers)
