class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [0] * N
        val = 1
        for i in range(N):
            prefix[i] = val
            val *= nums[i]
        
        val = 1
        for i in range(N-1,-1,-1):
            prefix[i] = prefix[i] * val
            val *= nums[i]
        
        return prefix