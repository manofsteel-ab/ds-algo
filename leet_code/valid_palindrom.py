"""
Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as
 valid palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_sz = len(s)
        if str_sz <= 1:
            return True

        start_idx = 0
        end_idx = str_sz - 1
        is_palindrom = True
        while start_idx < end_idx:
            char_1 = s[start_idx].lower()
            char_2 = s[end_idx].lower()
            if not char_1.isalnum():
                start_idx += 1
            elif not char_2.isalnum():
                end_idx -= 1
            elif char_1 == char_2:
                start_idx += 1
                end_idx -= 1
            else:
                is_palindrom = False
                break
        return is_palindrom
