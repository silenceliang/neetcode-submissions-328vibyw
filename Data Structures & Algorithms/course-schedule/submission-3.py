class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph[i] contains all courses that depend on course i
        graph = [[] for _ in range(numCourses)]
        
        # indegree[i] is the number of prerequisites course i still needs
        indegree = [0] * numCourses
        
        # Build the graph and indegree counts
        for tgt, src in prerequisites:
            graph[src].append(tgt)
            indegree[tgt] += 1
            
        # Initialize queue with all courses that have 0 prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        completed_courses = 0
        
        while queue:
            course = queue.popleft()
            completed_courses += 1
            
            for dependent_course in graph[course]:
                indegree[dependent_course] -= 1
                
                # If all prerequisites are met, it's ready to take
                if indegree[dependent_course] == 0:
                    queue.append(dependent_course)
                    
        # If we completed all courses, there was no cycle
        return completed_courses == numCourses