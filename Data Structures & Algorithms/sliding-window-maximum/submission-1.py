class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []
        for i in range(len(nums)):
            while h and h[0][1] + k <= i:
                heapq.heappop(h)
                
            heapq.heappush(h, (-nums[i], i))
            if len(h) >= k:
                res.append(-h[0][0])
        
        return res