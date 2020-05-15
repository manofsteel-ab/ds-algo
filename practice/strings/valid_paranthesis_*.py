class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True

        # treat "*" as left paranthesis

        count = 0
        for char in s:
            if char in ['(', '*']:
                count+=1
            else:
                count-=1
            if count<0:
                return False

        if count == 0:
            return True

        # if all above condition fail

        count=0
        for char in s[::-1]:
            if char in [')', '*']:
                count+=1
            else:
                count-=1

            if count<0:
                return False

        return True
        
