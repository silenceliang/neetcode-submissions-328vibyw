class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # element can be repetitive
        # avoid duplicate answer
        res = []
        def backtrack(cur, step, target):
            if target == 0:
                res.append(cur)
                return
            for i in range(step, len(nums)):
                if target-nums[i] < 0:
                    continue
                backtrack(cur+[nums[i]], i, target-nums[i])

        backtrack([], 0, target)
        return res