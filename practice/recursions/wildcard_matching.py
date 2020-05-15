class Solution:

    def _validate(self, input_str, pattern, input_idx, pat_idx, memo):
        if (input_idx,pat_idx) in memo:
            return memo[(input_idx,pat_idx)]
        if input_idx == len(input_str):
            for i in range(pat_idx, len(pattern)):
                if pattern[i]!='*':
                    return False
            return True
        if pat_idx == len(pattern):
            return False

        if pattern[pat_idx] == '*':
            star_as_empty = self._validate(input_str, pattern, input_idx, pat_idx+1, memo)
            start_as_non_empty = self._validate(input_str,pattern,input_idx+1,pat_idx, memo)
            memo[(input_idx,pat_idx)] = star_as_empty or start_as_non_empty

        if pattern[pat_idx] != '*':
            if input_str[input_idx] == pattern[pat_idx] or pattern[pat_idx] == '?':
                memo[(input_idx,pat_idx)] = self._validate(input_str,pattern,input_idx+1,pat_idx+1, memo)
            else:
                memo[(input_idx,pat_idx)] = False
        return memo[(input_idx,pat_idx)]

    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self._validate(s,p,0,0, memo)
