class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac_reachable = set()
        atl_reachable = set()
        
        def dfs(r, c, reachable, prev_height):
            # Stop if out of bounds, already visited, or water can't flow up to this cell
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                (r, c) in reachable or heights[r][c] < prev_height):
                return
            
            # Mark as reachable by the current ocean
            reachable.add((r, c))
            
            # Check all 4 directions
            dfs(r + 1, c, reachable, heights[r][c])
            dfs(r - 1, c, reachable, heights[r][c])
            dfs(r, c + 1, reachable, heights[r][c])
            dfs(r, c - 1, reachable, heights[r][c])
            
        # 1. Start DFS from the top and bottom rows
        for c in range(cols):
            dfs(0, c, pac_reachable, heights[0][c])         # Top row -> Pacific
            dfs(rows - 1, c, atl_reachable, heights[rows-1][c]) # Bottom row -> Atlantic
            
        # 2. Start DFS from the left and right columns
        for r in range(rows):
            dfs(r, 0, pac_reachable, heights[r][0])         # Left col -> Pacific
            dfs(r, cols - 1, atl_reachable, heights[r][cols-1]) # Right col -> Atlantic
            
        # 3. Find the intersection of cells reachable by both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac_reachable and (r, c) in atl_reachable:
                    res.append([r, c])
                    
        return res