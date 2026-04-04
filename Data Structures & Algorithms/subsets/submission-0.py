class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur, step, res):
            res.append(cur)
            if step >= len(nums):
                return
            for i in range(step, len(nums)):
                backtrack(cur + [nums[i]], i+1, res)
        res = []
        backtrack([], 0, res)
        return res