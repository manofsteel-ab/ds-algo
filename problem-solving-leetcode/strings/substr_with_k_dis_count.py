"""
Given a string of lowercase alphabets, count all possible substrings
(not necessarily distinct) that has exactly k distinct characters.
"""

class Solution:
    def countkDist(self, s, k):
        ans = 0
        sz = len(s)

        for i in range(sz):
            disCount = 0

            freq = [0]*27

            for j in range(i,sz):
                if(freq[ord(str1[j]) - 97] == 0):
                    disCount += 1

                freq[ord(str1[j]) - 97] +=1

                if disCount == k:
                    ans+=1

                if disCount>k:
                    break
        return ans
