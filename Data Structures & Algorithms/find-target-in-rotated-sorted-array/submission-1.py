class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        #first find the min_idx

        while(left < right):
            mid = (left + right)//2
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
        #nums = [3,5,6,0,1,2], target = 4
        #0,5, 2;3,5,4;3,4,3;3,3
        #left will be at min val
        min_idx = left
        # now search for target
        if target == nums[min_idx]:
            return min_idx
        elif target > nums[-1]:
            #binary search target in left
            left = 0
            right = min_idx-1
        else:
            #binary search target in right
            left = min_idx+1
            right = len(nums)-1
        #0,2,1,0,0,0;1,0
        while(left<=right):
            mid = (left + right)//2
            if nums[mid] ==target:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        
        return -1
        