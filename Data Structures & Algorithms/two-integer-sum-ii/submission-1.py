class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        for i in range(N-1):
            item = numbers[i]
            l, r = i+1, N-1
            while l <= r:
                mid = l+(r-l)//2
                if numbers[mid] == target-item:
                    return [i+1, mid+1]
                elif numbers[mid] > target-item:
                    r = mid-1
                else:
                    l = mid+1
        return None