class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for end, start in prerequisites:
            g[start].append(end)
            indegree[end]+=1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        completed_courses = 0
        while q:
            x = q.popleft()
            completed_courses += 1
            order.append(x)
            for nei in g[x]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if completed_courses != numCourses:
            return []

        return order