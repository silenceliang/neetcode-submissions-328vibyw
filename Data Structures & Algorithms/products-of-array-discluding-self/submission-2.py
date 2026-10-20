class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_prod = [1]*N
        for i in range(1, N):
            prefix_prod[i] = prefix_prod[i-1]*nums[i-1]
        res = [0]*N
        cur = 1
        for i in range(N-1, -1, -1):
            res[i] = prefix_prod[i]*cur
            cur *= nums[i]
            
        return res