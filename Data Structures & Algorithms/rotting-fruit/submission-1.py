class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_oranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0
        
        rounds = 0
        while q:
            for _ in range(len(q)):
                (x, y) = q.popleft()
                for (dx, dy) in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nx = x+dx
                    ny = y+dy
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != 1:
                        continue
                    
                    grid[nx][ny] = 2
                    fresh_oranges -= 1
                    q.append((nx, ny))

            if q:
                rounds += 1

        return rounds if fresh_oranges == 0 else -1