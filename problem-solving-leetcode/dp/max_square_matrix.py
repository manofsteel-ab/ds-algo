class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*cols for i in range(rows)]
        square_size = 0
        for i in range(rows):
            if matrix[i][0] == '1':
                square_size = 1
            dp[i][0] = int(matrix[i][0])

        for j in range(cols):
            if matrix[0][j] == '1':
                square_size = 1
            dp[0][j] = int(matrix[0][j])


        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
                square_size = max(square_size, dp[i][j])
        return square_size*square_size

        
