class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # element can be repetitive
        # avoid duplicate answer
        def backtrack(cur, target, res):
            if target<0:
                return
            if target==0:
                candidcate = sorted(cur)
                if candidcate not in res:
                    res.append(candidcate)
                return
            for i in range(len(nums)):
                backtrack(cur+[nums[i]], target-nums[i], res)
        res = []
        backtrack([], target, res)
        return res