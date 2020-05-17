"""
Given an integer array nums, find the sum of the elements between indices i and
j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to
val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.sz = len(nums)
        self.bit = [0]*(self.sz+1)
        self.nums = nums

        for i in range(self.sz):
            self.add(i + 1,nums[i])

    def add(self, index, val):
        while index <= self.sz:
            self.bit[index] += val
            index += index & -index

    def get_sum(self,index):
        res = 0
        while index>0:
            res += self.bit[index]
            index -= index & -index
        return res

    def update(self, index, val):
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, i: int, j: int) -> int:
        if not self.nums:
            return 0
        sum1 = self.get_sum(j+1)
        sum2 = self.get_sum(i)

        return sum1-sum2



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
