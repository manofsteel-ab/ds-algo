class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or max(nums)<0:
            return 1

        sz = len(nums)

        for i in range(sz):

            # if value is <=0 or >sz ignore them

            if nums[i]<=0 or nums[i]>sz:
                continue

            val = nums[i]


            # traver until we reach at the element that already marked or we can not mark
            while nums[val-1] != val:
                next_element = nums[val-1] # store before marking
                nums[val-1] = val # mark
                val = next_element # go to next

                if val<=0 or val>sz:
                    break
        for i in range(sz):
            if nums[i]!=i+1:
                return i+1
        return sz+1
