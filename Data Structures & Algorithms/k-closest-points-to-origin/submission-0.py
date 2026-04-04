class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p1,p2 in points:
            dis = p1**2+p2**2
            heapq.heappush(h, (dis, (p1, p2)))
        res = []
        while k > 0:
            res.append(heapq.heappop(h)[1])
            k-=1
        return res