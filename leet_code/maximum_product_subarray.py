class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        sz  = len(nums)
        if sz == 0:
            return 0
        ans = nums[0]
        minProduct = nums[0]
        maxProduct = nums[0]
        for i in range(1, sz):
            if nums[i]<0:
                minProduct, maxProduct = maxProduct, minProduct

            minProduct = min(nums[i], minProduct*nums[i])
            maxProduct = max(nums[i], maxProduct*nums[i])
            ans = max(maxProduct, ans)

        return ans
