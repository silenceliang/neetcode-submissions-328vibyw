class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1] * (N+1)
        for i in range(1, N):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        suffix = 1
        res = [0]*N
        for i in range(N-1,-1,-1):
            res[i] = suffix*prefix[i]
            suffix *= nums[i]
            
        return res