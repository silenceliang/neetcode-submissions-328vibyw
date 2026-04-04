class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r-l)//2
            take = 0
            for p in piles:
                take += p // mid
                if p % mid > 0:
                    take += 1
            if take > h:
                l = mid+1
            else:
                r = mid-1

        return r+1