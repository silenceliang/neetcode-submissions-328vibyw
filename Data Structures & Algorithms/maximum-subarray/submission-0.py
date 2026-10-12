class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -0xfffffff
        total = 0
        for i in range(len(nums)):
            if total < 0:
                total = 0
            total += nums[i]
            max_sum = max(max_sum, total)
            
        return max_sum