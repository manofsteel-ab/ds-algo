class Solution:
    def findMin(self, nums):
        sz = len(nums)
        if sz == 0:
            return -1

        if sz==1:
            return nums[0]

        low = 0
        high = sz-1

        if nums[low]<=nums[high]:
            return nums[low]

        while low<high:
            mid = (low+high)//2

            if mid<high and nums[mid+1]<nums[mid]:
                return nums[mid+1]

            if mid>low and nums[mid-1]>nums[mid]:
                return nums[mid]

            if nums[mid]>nums[0]:
                low = mid+1
            else:
                high = mid-1
        return -1
