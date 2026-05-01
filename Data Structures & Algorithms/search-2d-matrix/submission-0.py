class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # i am thinking, it is like a binary search on arr of size: m*n
        # looks exactly same since i do not need to return the i,j even
        # just true or false
        # i may need to get i,j based on mid of arr to look if it matches
        # mid_i_j = f(mid); eg mid = 6, 6%n-1 or (6%4)-1=1 will be j & 6//4 i

        # let's try recursive approach
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows*cols -1
        # analyse the empty case later [[]] 

        while(left<=right):
            mid = (left+right)//2
            mid_i, mid_j = mid//cols, mid%cols

            if matrix[mid_i][mid_j]== target:
                return True
            
            elif  matrix[mid_i][mid_j]> target:
                right = mid-1
            else:
                left = mid+1
        return False

        #run some test cases: 
        # target not there e.g 3, r,c = 3, 4, l,r = 0,11, 
        # 0<11 , m=5, mi, mj = 1, 1, mat_val = 11, target 3 < 11
        # r=5-1=4, m=2, mi, mj=0,2, val = 4, target 3<4
        # r = 2-1=1, m=0, mi, mj=0,0, val =1 3>1
        # l = 1,r=1, m =1, mi, mj=0,1, val=2 3>2
        # l = 2,r=1 l<=r not true, while closes, returns False,
        
        