class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix) 
        n = len(matrix[0])
        l = 0 
        r = m * n - 1
        while l <= r:
            mid = (l + r) // 2
            mid_value = matrix[mid // n][mid % n]
            if mid_value == target:
                return True
            elif mid_value < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
