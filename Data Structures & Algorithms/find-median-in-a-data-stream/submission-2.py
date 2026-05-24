class MedianFinder:

    def __init__(self):
        self.minh = [] # record [n/2, .., n]
        self.maxh = [] # record [0,...,n/2-1]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxh, -num)
        heapq.heappush(self.minh, -heapq.heappop(self.maxh))
        if len(self.maxh) < len(self.minh):
            heapq.heappush(self.maxh, -heapq.heappop(self.minh))

    def findMedian(self) -> float:
        if len(self.maxh) > len(self.minh):
            return -self.maxh[0]
        return (-self.maxh[0] + self.minh[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()