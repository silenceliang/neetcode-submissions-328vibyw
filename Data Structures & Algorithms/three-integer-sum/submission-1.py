class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []
        for i in range(N):
            cur = nums[i]
       
            if cur > 0:
                break

            if i > 0 and cur == nums[i-1]:
                continue
            
            l, r = i+1, N-1
            while l < r:
                total = cur + nums[l] + nums[r]
                if total > 0:
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    res.append([cur, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        
        return res