class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            if x & 1 << i > 0:
                return i
            x = x | 1<<i
        return -1