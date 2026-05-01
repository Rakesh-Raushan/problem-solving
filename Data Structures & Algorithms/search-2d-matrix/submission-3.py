class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows*cols-1

        while left <= right:
            mid = (left+right)//2
            mid_val = matrix[mid//cols][mid%cols]
            if target == mid_val:
                return True
            elif target > mid_val:
                # search right
                left = mid+1
            else:
                right = mid-1
        
        return False