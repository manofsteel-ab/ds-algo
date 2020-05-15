class Solution:
    def stringShift(self, s, shift):
        if not shift or not s:
            return s

        left_shift = 0
        right_shift = 0
        sz = len(s)
        for val in shift:
            if val[0] == 0:
                left_shift+=val[1]
            else:
                right_shift+=val[1]

        diff = left_shift-right_shift

        if diff == 0:
            return s
        total_shift = abs(diff)%sz
        if diff>0:
            return s[total_shift:]+s[:total_shift]
        else:
            return s[sz-total_shift:]+s[:sz-total_shift]
