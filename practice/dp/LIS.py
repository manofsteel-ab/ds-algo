class Solution:

    def _getIndex(self, nums, target):
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low+high)//2

            if nums[mid]>=target:
                high = mid-1
            else:
                low = mid+1
        return low


    def N_LOG_N(self, nums):
        if not nums:
            return 0

        sz = len(nums)
        ans = []
        for val in nums:
            if not ans or val>ans[-1]:
                ans.append(val)
            elif val<=ans[0]:
                ans[0] = val
            else:

                idx = self._getIndex(ans,val)
                ans[idx] = val
        return len(ans)

    def N_Square(self, nums):
        if not nums:
            return 0
        sz = len(nums)
        dp = [1]*(sz)

        for i in range(1, sz):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j] and  dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.N_LOG_N(nums)
