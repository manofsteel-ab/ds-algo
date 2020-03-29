class Solution:
    def myAtoi(self, s: str):
        ans = 0
        s = s.lstrip()
        isNeg = False
        if not s:
            return 0
        elif s[0] == '-':
            s = s[1:]
            isNeg = True
        elif s[0] == '+':
            s = s[1:]
        for val in s:
            if val not in "0123456789":
                break
            else:
                ans = ans*10 + int(val)

        if isNeg:
            ans = ans*-1
        if ans<-2147483648:
            return -2147483648
        if ans>2147483647:
            return 2147483647
        return ans
