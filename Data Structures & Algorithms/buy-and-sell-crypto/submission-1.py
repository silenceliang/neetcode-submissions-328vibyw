class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = 0xfffffff
        for i in prices:
            min_buy = min(min_buy, i)
            profit = max(profit, i-min_buy)
        return profit