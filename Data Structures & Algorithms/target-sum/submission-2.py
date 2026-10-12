class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}  # Cache to store results of (idx, cur)
        N = len(nums)
        
        def backtrack(idx, cur):
            if (idx, cur) in memo:
                return memo[(idx, cur)]
            
            if idx == N:
                return 1 if cur == target else 0
            
            add = backtrack(idx + 1, cur + nums[idx])
            subtract = backtrack(idx + 1, cur - nums[idx])
            
            memo[(idx, cur)] = add + subtract
            return memo[(idx, cur)]
        
        return backtrack(0, 0)