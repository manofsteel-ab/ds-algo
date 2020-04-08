class Solution:

    def _upperBound(self, nums, low, high, target):
        if low>high:
            return -1
        maxIndex = high
        while low<=high:
            mid = (low+high)//2

            if nums[mid] == target and (mid == maxIndex or nums[mid+1]>target):
                return mid
            if nums[mid]<=target:
                low = mid+1
            else:
                high = mid-1
        return -1

    def _lowerBound(self, nums, low, high, target):
        if low>high:
            return -1

        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target and (mid==0 or nums[mid-1]<target):
                return mid
            if nums[mid]>=target:
                high = mid-1
            else:
                low = mid+1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        lowerIndex = self._lowerBound(nums, low, high, target)
        higherIndex = self._upperBound(nums, low, high, target)
        return [lowerIndex,higherIndex]
