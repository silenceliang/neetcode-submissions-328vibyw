import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # pq (freq, [number,])
        freq = [0]*2001
        for n in nums:
            freq[n+1000] += 1
        
        pq = []
        for i in range(2001):
            heapq.heappush(pq, (-freq[i], i-1000))
        res = []
        for i in range(k):
            _, item = heapq.heappop(pq)
            res.append(item)
        return res