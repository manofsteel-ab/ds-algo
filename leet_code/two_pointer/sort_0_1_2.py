class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sz = len(nums)
        if sz<=1:
            return

        low = 0 # upper bound of 0
        mid = 0 # iterator
        high = sz-1  # lower bound of 2

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
        
