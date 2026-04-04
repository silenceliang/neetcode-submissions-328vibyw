class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_m = [0]*26
        for i in tasks:
            task_m[ord(i) - ord('A')]+=1
        h = []
        for i in range(26):
            if task_m[i] == 0:
                continue
            heapq.heappush(h, -task_m[i])

        time = 0
        q = deque() # store [freq of task, time]
        # keep the early event in the front
        while h or q:
            time += 1
            if h:
                freq = heapq.heappop(h) + 1
                if freq != 0:
                    q.append([freq, time+n])            
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])

        return time
            