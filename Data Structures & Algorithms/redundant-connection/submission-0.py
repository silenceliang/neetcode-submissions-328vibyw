class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        
        def dfs(i, parent):
            if visited[i]:
                return True 

            visited[i] = True
            for nei in adj[i]:
                if nei == parent:
                    continue
                if dfs(nei, i):
                    return True
            return False

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visited = [False]*(n+1)
            
            if dfs(a, -1):
                return [a,b]
        return []

