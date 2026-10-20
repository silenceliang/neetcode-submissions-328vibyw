class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        for i in range(N):
            l, r = i+1, N-1
            left = target - numbers[i]
            while l <= r:
                mid = l+(r-l)//2
                if numbers[mid] == left:
                    return [i+1, mid+1]
                elif numbers[mid] < left:
                    l = mid+1
                else:
                    r = mid-1
        return None