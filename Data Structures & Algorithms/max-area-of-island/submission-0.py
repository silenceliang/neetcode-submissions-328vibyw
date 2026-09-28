class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            total = 0
            for (dx, dy) in [[1,0],[0,1],[-1,0],[0,-1]]:
                total += dfs(i+dx, j+dy)
            return total + 1

        res = 0      
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
                    
        return res