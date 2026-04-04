class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        l, r = 0, N-1
        leftMax, rightMax = height[0], height[N-1]
        res = 0
        while l < r:
            if height[l] <= height[r]:
                res += leftMax - height[l]
                l+=1
                leftMax = max(leftMax, height[l])
            else:
                res += rightMax - height[r]
                r-=1
                rightMax = max(rightMax, height[r])

        return res
