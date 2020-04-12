class Solution:

    def dfs(self,i,j, grid, visited, rows, cols):
        if i<0 or i>=rows:
            return
        if j<0 or j>=cols:
            return

        if visited[i][j]:
            return

        if grid[i][j]!='1':
            return

        visited[i][j] = True
        directionX = [1,-1,0,0]
        directionY = [0,0,1,-1]

        for c in range(4):
            x = i+directionX[c]
            y = j+directionY[c]
            self.dfs(x,y,grid,visited,rows,cols)

    def numIslands(self, grid: List[List[str]]) -> int:

        ans = 0
        if not grid:
            return ans
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False]*cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    ans+=1
                    self.dfs(i,j,grid,visited,rows,cols)
        return ans
