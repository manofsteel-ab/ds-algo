class Solution:

    def N2(self, nums):
        """
         O(N^2) approach
        """
        nums = [str(val) for val in nums]
        n  = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                a,b = nums[i], nums[j]
                if int(a+b)<int(b+a):
                    nums[i], nums[j] = nums[j], nums[i]
        ans =  "".join(nums)
        if int(ans) == 0:
            return "0"
        return ans

    def NLOGN(self, nums):
        string_nums = list(map(str, nums))
        max_len = max([len(x) for x in string_nums])

        for i in range(max_len, -1, -1):
            string_nums = sorted(string_nums, key = lambda x: x[i%len(x)], reverse=True)

        return str(int("".join(string_nums)))

    def largestNumber(self, nums: List[int]) -> str:
        return self.NLOGN(nums)
        
