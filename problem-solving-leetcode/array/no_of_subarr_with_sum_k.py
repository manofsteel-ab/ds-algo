class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        hash_map = defaultdict(lambda:0)
        ans = 0
        cum_sum = 0
        for val in nums:
            cum_sum+=val
            if cum_sum == k:
                ans+=1
            if hash_map.get(cum_sum-k):
                ans+=hash_map.get(cum_sum-k)
            hash_map[cum_sum]+=1
        return ans
        
