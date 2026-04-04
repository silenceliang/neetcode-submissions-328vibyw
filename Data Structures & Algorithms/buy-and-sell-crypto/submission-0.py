class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = 101
        res = 0
        for i in prices:
            if i < cur_min:
                cur_min = i
            res = max(res, i-cur_min)
        return res
