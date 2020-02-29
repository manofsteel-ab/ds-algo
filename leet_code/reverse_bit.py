"""
Reverse bits of a given 32 bits unsigned integer.



Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100
represents the unsigned integer 43261596, so return 964176192 which its binary
representation is 00111001011110000010100101000000.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        a = '{0:032b}'.format(n)
        reverse = a[::-1]
        return int(reverse, 2)


class Solution2:
    def reverseBits(self, n: int) -> int:
        ans = 0
        bit = 0
        while bit<32:
            if n%2:
                ans = ans*2+1
            else:
                ans = ans*2 + 0
            n >>=1
            bit +=1
        return ans