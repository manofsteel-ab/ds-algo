

class Solution:

    def _generate(self, numbers, current_index, ans):

        if len(numbers) == current_index:
            ans.append(numbers[:])
            return

        for i in range(current_index,len(numbers)):
            numbers[current_index], numbers[i] = numbers[i], numbers[current_index]
            self._generate(numbers, current_index+1, ans)
            numbers[current_index], numbers[i] = numbers[i], numbers[current_index]

    def permute(self, nums):

        ans = []

        self._generate(nums, 0, ans)
        return ans
