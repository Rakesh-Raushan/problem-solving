class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # left, right = 0, len(nums)-1

        # while(left <= right):
        #     mid = (right+left)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif target < nums[mid]:
        #         right = mid-1
        #     else:
        #         left = mid+1
        # return -1
        # let's try recursive

        def binary_search(arr, start, end, target):
            if start>end:
                return -1
            mid = (start+end)//2
            if arr[mid]== target:
                return mid
            elif target < arr[mid]:
                return binary_search(arr, start, mid-1, target)
            else:
                return binary_search(arr, mid+1, end, target)
        
        return binary_search(nums, 0, len(nums)-1, target)

        