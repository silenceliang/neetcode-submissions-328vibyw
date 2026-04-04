class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        res = [0]*n
        step = 0
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                res[step] = nums1[i]
                i+=1
            else:
                res[step] = nums2[j]
                j+=1

            step+=1
        
        while i < n1:
            res[step] = nums1[i]
            i+=1
            step+=1
        
        while j < n2:
            res[step] = nums2[j]
            j+=1
            step+=1
        
        if n%2==1:
            return res[n//2] 
        
        return (res[n//2] + res[n//2-1]) / 2
        