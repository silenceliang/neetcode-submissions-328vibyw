class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # break down to one dim?
        # move up or down, left or right
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            mid = l + (r-l)//2
            new_row = mid // n
            new_col = mid % n
            if target == matrix[new_row][new_col]:
                return True 
            if target > matrix[new_row][new_col]:
                l = mid+1
            else:
                r = mid-1
        return False