"""

You have given an array of positive integer. You have to find the total number
of subarray having exactly k distinct element

Approach - To directly find the subarray with exactly k diff element is hard.
But to find a subarray with atmost k different element is easy.

Let's suppose no of subarray with atmost k different element is C(k).
and no of subarray with atmost k-1 diff element is C(k-1)

so no of subarray with exactly k diff element  = C(k) - C(k-1)

Now to count the subarray with atmost k diff element, we can use sliding window
approach. The idea is to keep expanding the right boundry till the count of distinct
element is less or equal to k. when count of distinct element becomes more than k
start shrinking the window from left till the count becomes less or equal to k.

"""

# from collections import OrderedDict

class Solution:
    def count_with_atmost_k_diff(self, array, k):
        if not array:
            return 0

        window = {}
        left = 0
        right = 0
        count = 0
        while right<len(array):

            if array[right] not in window:
                window[array[right]] = 0

            window[array[right]]+=1

            while len(window)>k:

                window[array[left]]-=1

                if window[array[left]] == 0:
                    del window[array[left]]
                left+=1

            count+=right - left + 1
            right+=1
        return count
    def subarraysWithKDistinct(self, array: List[int], k: int) -> int:
        return self.count_with_atmost_k_diff(
            array,k
        ) - self.count_with_atmost_k_diff(array,k-1)
