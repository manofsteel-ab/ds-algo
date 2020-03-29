class Solution:
    def isValid(self, i, j, rows, cols):
        return i>=0 and i<rows and j>=0 and j<cols

    def dfs(self, i, j, visited, board, rows, cols):
        visited[i][j] = True
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        for direction in directions:
            newI = i+direction[0]
            newJ = j+direction[1]
            if self.isValid(newI, newJ, rows, cols) and not visited[newI][newJ] and board[newI][newJ] == 'O':
                self.dfs(newI, newJ, visited, board, rows, cols)

    def solve(self, board):
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        visited = [[False]*cols for _ in range(rows)]

        for i in range(rows):
            if board[i][0]=='O':
                self.dfs(i,0,visited,board,rows,cols)
            if board[i][cols-1]=='O':
                self.dfs(i,cols-1,visited,board,rows,cols)
        for j in range(cols):
            if board[0][j]=='O':
                self.dfs(0,j, visited,board,rows,cols)
            if board[rows-1][j]=='O':
                self.dfs(rows-1,j,visited,board,rows,cols)

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and not visited[i][j]:
                    board[i][j]='X'
			
