class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        def backtrack(cur, left):
            if len(left) == 0:
                res.append(cur)
                return
            for i in range(len(left)):
                backtrack(cur + [left[i]], left[:i] + left[i+1:])
        backtrack([], nums)
        return res