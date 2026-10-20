class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in nums:
            if i in h:
                return True
            h[i] = True
        return False
        