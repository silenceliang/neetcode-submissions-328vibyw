class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, -n)
        res = 0
        while k > 0:
            res = -heapq.heappop(h)
            k-=1
        return res