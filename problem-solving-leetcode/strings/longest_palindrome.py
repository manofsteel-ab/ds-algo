class Solution:

    def getOddLenthLongestpalindrome(self, s):
        sz = len(s)
        ans = s[0]
        mx = 1
        for i in range(1,sz):
            prev = i-1
            nxt = i+1
            cnt = 1
            while prev>=0 and nxt<sz and s[prev] == s[nxt]:
                if nxt-prev+1>mx:
                    mx = nxt-prev+1
                    ans = s[prev:nxt+1]
                prev-=1
                nxt+=1
        return ans

    def getEvenLenthLongestpalindrome(self, s):
        sz = len(s)
        ans = ""
        mx = 0
        for i in range(1,sz):
            if s[i]!=s[i-1]:
                continue
            prev = i-1
            nxt = i

            while prev>=0 and nxt<sz and s[prev] == s[nxt]:
                if nxt-prev+1>mx:
                    mx = nxt-prev+1
                    ans = s[prev:nxt+1]
                prev-=1
                nxt+=1
        return ans


    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s

        ans1 = self.getOddLenthLongestpalindrome(s)
        ans2 = self.getEvenLenthLongestpalindrome(s)
        if len(ans1)>len(ans2):
            return ans1
        return ans2
