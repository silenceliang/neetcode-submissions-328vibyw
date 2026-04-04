class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = sorted(nums)
        
    def add(self, val: int) -> int:
        l, r = 0, len(self.arr)-1
        while l <= r:
            m = l+(r-l)//2
            if self.arr[m] > val:
                r = m-1
            else:
                l = m+1
        
        self.arr = self.arr[:l] + [val] + self.arr[l:]

        return self.arr[-self.k]
