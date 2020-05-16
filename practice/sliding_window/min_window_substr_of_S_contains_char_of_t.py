"""
Given a string S and a string T, find the minimum window in S which will contain
 all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the
empty string "".
If there is such window, you are guaranteed that there will always be only one
unique minimum window in S.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t and not s:
            return ""

        t_char_counter = Counter(t)
        left = 0
        right = 0
        window_counter = {}
        t_char_count_in_window = 0

        diff = float(inf)
        ans = ""
        while right<len(s):
            char = s[right]
            window_counter[char] = window_counter.get(char,0)+1

            if char in t_char_counter and (
                t_char_counter[char] ==  window_counter[char]
            ): # if char freq in window and t are same
                t_char_count_in_window+=1
            # print(t_char_counter,window_counter, t_char_count_in_window)
            while left<=right and t_char_count_in_window == len(t_char_counter.keys()):
                # print(left,right)
                if diff > right-left+1:
                    diff = right-left+1
                    ans = s[left:right+1]
                # print(ans)
                left_char = s[left]
                window_counter[left_char]-=1
                # print(left_char in t_char_counter,)
                if left_char in t_char_counter and (
                    window_counter[left_char]<t_char_counter[left_char]
                ):
                    t_char_count_in_window-=1
                # print(window_counter,left_char,t_char_count_in_window)
                left+=1
            right+=1
        return ans
