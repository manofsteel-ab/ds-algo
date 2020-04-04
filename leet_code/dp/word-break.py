"""
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the
segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as
"apple pen apple".
 Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDictSize = len(wordDict)
        if wordDictSize == 0:
            return False
        str_sz = len(s)
        dp = [False] * (str_sz + 1)
        dp[0] = True

        for i in range(1, str_sz + 1):
            dp[i] = False
            j = i - 1
            while j >= 0:
                if dp[j] is True:
                    substr = s[j:i]
                    if substr in wordDict:
                        dp[i] = True
                        break
                j -= 1
        return dp[str_sz]



