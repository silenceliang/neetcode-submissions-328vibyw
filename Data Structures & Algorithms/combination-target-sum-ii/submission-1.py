class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(cur, target, step):
            if target < 0:
                return
            if target == 0:
                res.append(cur)
                return
            for i in range(step, len(candidates)):
                if i > step and candidates[i-1] == candidates[i]:
                    continue
                backtrack(cur+[candidates[i]], target-candidates[i], i+1)
        
        backtrack([], target, 0)
        return res