class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        freq_dict = {}
        ans = 0
        start_idx = 0
        for index,char in enumerate(s):
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1

            if freq_dict[char] == 1:
                ans = max(ans, index-start_idx)
            else:
                while start_idx<index and freq_dict[char]>1:
                    freq_dict[s[start_idx]]-=1
                    start_idx+=1
        return ans+1
