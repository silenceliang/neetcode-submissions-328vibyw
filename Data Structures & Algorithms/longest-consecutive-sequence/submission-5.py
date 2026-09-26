class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = Counter(nums)
        N = len(nums)
        res = 0
        for i in range(N):
            if nums[i]-1 in freq:
                continue
            next_nums = nums[i] + 1
            c = 1
            while next_nums in freq:
                c+=1
                next_nums+=1
            res = max(res, c)

        return res
