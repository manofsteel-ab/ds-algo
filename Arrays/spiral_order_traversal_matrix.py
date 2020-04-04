class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans = []

        rows = len(matrix)
        cols = len(matrix[0])
        r = 0
        c = 0
        while r<rows and c<cols:
            # TOP ROW    
            for i in range(c, cols):
                ans.append(matrix[r][i])
            r+=1

            #RIGHT COL
            for i in range(r, rows):
                ans.append(matrix[i][cols-1])
            cols-=1

            #bottom row
            if r<rows:
                for i in range(cols-1, c-1, -1):
                    ans.append(matrix[rows-1][i])
                rows-=1
            #left COL
            if c<cols:
                for i in range(rows-1, r-1, -1):
                    ans.append(matrix[i][c])
                c+=1
        return ans
