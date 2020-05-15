class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        freq = Counter(s)
        sz = len(s)
        flag = True
        for key in freq:
            if freq.get(key)<k:
                flag = False

        if flag:
            return sz
        maxLen = 0
        start = 0
        for i in range(sz):
            if freq[s[i]]<k:
                maxLen = max(maxLen, self.longestSubstring(s[start:i], k))
                start = i+1
        maxLen = max(maxLen, self.longestSubstring(s[start:], k))
        return maxLen
