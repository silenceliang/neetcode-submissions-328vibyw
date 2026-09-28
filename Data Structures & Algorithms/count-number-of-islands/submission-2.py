class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        def dfs(i, j):
            if i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] == '0':
                return
            grid[i][j] ='0'
            for (dx, dy) in [[1,0],[0,1],[-1,0],[0,-1]]:
                dfs(i+dx, j+dy)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res