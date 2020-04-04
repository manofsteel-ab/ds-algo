class Solution1:

    # def _lowerBound(self,)

    def searchRange(self, nums, target: int):
        try:
            index1 = nums.index(target)
        except ValueError:
            index1 = -1

        try:
            index2 = len(nums) - 1 - nums[::-1].index(target)
        except ValueError:
            index2 = -1
        return [index1, index2]


class Solution:

    def _lowerBound(self, nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 or nums[mid - 1] < target) and nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def _upperBound(self, nums, low, high, target):
        n = high
        while low <= high:
            mid = (low + high) // 2
            if (mid == n or nums[mid + 1] > target) and nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def searchRange(self, nums, target):
        n = len(nums)
        index1 = self._lowerBound(nums, 0, n - 1, target)
        index2 = self._upperBound(nums, 0, n - 1, target)
        # print(index1, index2)
        return [index1, index2]