class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # #iterative
        # left, right = 0, len(nums)-1

        # while left <= right:
        #     mid = (left+right)//2
        #     if target == nums[mid]:
        #         return mid
        #     elif target < nums[mid]:
        #         #search left half
        #         right = mid - 1
        #     else:
        #         #search right half
        #         left = mid + 1
        
        # return -1

        #recursive
        def helper(left,right):
            if left > right:
                return None
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return helper(left, mid-1)
            else:
                return helper(mid+1, right)
        result = helper(0,len(nums)-1)
        return  result if result is not None else -1

        
    # verify [-1,0,2,4] 0,3,m=1, 0<4
    #left =2,right=3,m=2,2<4,
    #left=3,right=3 m=3, return 3
    #search for -1, 0,3,m=1, 0>-1
    #left=0,right = 0, found