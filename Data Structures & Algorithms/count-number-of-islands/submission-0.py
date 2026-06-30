class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row, col):
            if row <0 or row >= m or col < 0 or col >=n or grid[row][col]=="0":
                return 
            grid[row][col] = "0"
            for dx,dy in directions:
                dfs(row+dx,col+dy)
            return 
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    ans +=1
                    dfs(i,j)
        return ans
            