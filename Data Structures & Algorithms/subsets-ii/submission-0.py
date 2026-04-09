class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []
        def backtrack(start, subset):
            res.append(subset)
            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                backtrack(i+1, subset + [nums[i]])
        
        backtrack(0, [])
        return res