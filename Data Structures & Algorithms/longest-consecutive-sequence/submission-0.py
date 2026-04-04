class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        longest = 0
        for i in m:
            w = i
            cur = 1
            while w+1 in m:
                cur+=1
                w+=1
            longest = max(longest, cur)
        return longest