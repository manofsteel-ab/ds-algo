"""
number               0000 0000 0000 0000 0000 0000 0101 1100
~number              1111 1111 1111 1111 1111 1111 1010 0011
(~number) + 1        1111 1111 1111 1111 1111 1111 1010 0100
-number              1111 1111 1111 1111 1111 1111 1010 0100
(number) & (-number) 0000 0000 0000 0000 0000 0000 0000 0100
You can see from the example above that (number) & (-number) gives you the least bit.
"""


class BIT:

    def __init__(self, n):
        self.bit = [0]*(n+1)
        self.sz = n


    def get_sum(self, index):

        i = index+1 # 1 base indexing
        s = 0

        while i>0:
            s+=self.bit[i]
            i-=i&-i
        return s

    def update(self, index, val):
        i = index+1

        while i<=sz:
            self.bit[i]+=val
            i+=i&-i
