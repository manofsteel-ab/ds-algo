class Solution:
    def _bsearch(self, nums, target, low, high):
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid]<nums[high]:
                if target>nums[mid] and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if target>=nums[low] and target<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1

        return -1


    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        sz = len(nums)
        return self._bsearch(nums, target, 0, sz-1)
