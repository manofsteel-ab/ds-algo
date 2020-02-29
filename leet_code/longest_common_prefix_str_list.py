"""
Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:

    def _bruteForce(self, string_list):
        commonPrifix = ""
        list_sz = len(string_list)
        if not list_sz:
            return commonPrifix
        max_index = min([len(val) for val in string_list])

        current_index = 0
        while current_index < max_index:
            char = ""
            matched = True
            for i in range(0, list_sz):
                if i == 0:
                    char = string_list[i][current_index]
                    continue

                if char != string_list[i][current_index]:
                    matched = False
                    break
            if not matched:
                break

            commonPrifix += char
            current_index += 1
        return commonPrifix

    def longestCommonPrefixUsingZip(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                p += x
            else:
                break
        return p

    def longestCommonPrefix(self, strs) -> str:
        return self._bruteForce(strs)

