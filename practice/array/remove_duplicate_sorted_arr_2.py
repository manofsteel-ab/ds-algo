class Solution:
    def removeDuplicates(self, nums) -> int:
        sz = len(nums)

        if sz<2:
            return sz

        count=0
        i=0
        j=0
        prev = nums[0]
        while i<sz:
            if nums[i] == prev and j<2:
                nums[count] = prev
                count+=1
                i+=1
                j+=1
            elif nums[i] == prev and j>=2:
                i+=1
            else:
                prev = nums[i]
                j = 0
        # print(nums)
        return count
