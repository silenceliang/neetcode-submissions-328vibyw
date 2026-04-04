class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left_prefix = [0]*N
        right_prefix = [0]*N
        left_prefix[0] = height[0]
        for i in range(1,N):
            left_prefix[i] = max(left_prefix[i-1], height[i])
        right_prefix[N-1] = height[N-1]
        for i in range(N-2,-1,-1):
            right_prefix[i] = max(right_prefix[i+1], height[i])
        
        res = 0
        for i in range(N):
            res+=min(left_prefix[i],right_prefix[i])- height[i]
        return res