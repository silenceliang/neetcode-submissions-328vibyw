class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        # Use a deque for O(1) pops from the left (Breadth-First Search)
        q = deque()
        
        # 1. Add all treasures (0s) to the queue to start a multi-source BFS
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    
        # 2. Process the queue
        while q:
            x, y = q.popleft() # Pop 2 items, matching what we appended
            
            for dx, dy in [[1,0], [0,1], [-1,0], [0,-1]]:
                next_x, next_y = x + dx, y + dy
                
                # Check bounds
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue
                
                # In this problem, empty rooms are initialized to 2147483647
                # If a cell is -1 (water), 0 (treasure), or already visited (distance < INF), skip it.
                if grid[next_x][next_y] != 2147483647:
                    continue
                    
                # Because we are using BFS, the first time we reach a room is guaranteed 
                # to be the shortest distance. Update it and add to the queue.
                grid[next_x][next_y] = grid[x][y] + 1
                q.append((next_x, next_y))