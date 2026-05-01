class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n_rows, n_cols = len(matrix), len(matrix[0])
        left, right= 0, n_rows*n_cols - 1

        while(left<=right):
            mid = (left+right)//2
            mid_row = mid//n_cols
            mid_col = mid%n_cols
            mid_val=matrix[mid_row][mid_col]

            if target == mid_val:
                return True
            elif target > mid_val:
                left = mid+1
            else:
                right = mid-1
        
        return False
        