class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-i for i in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            y, x = -heapq.heappop(neg_stones), -heapq.heappop(neg_stones)
            heapq.heappush(neg_stones, -(y-x))
        return -neg_stones[0] if len(neg_stones) > 0 else 0