class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums)

    #     while(left <= right):
    #         #calculate the mid index for this array
    #         mid = (left+right)//2
    #         #compare to target
    #         if target == nums[mid]:
    #             return mid
    #         elif target > nums[mid]:
    #             left = mid+1
    #         else:
    #             right = mid-1
        
    #     return -1
    #above is the binary iterative versio with O(logn) time and O(1) space
    #if recursive is asked explicitly then only go for it as it has both time and space O(logn)
    #recursive solution
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        return self.helper(left,right,nums,target)
    
    def helper(self,left,right,nums,target):
        if left > right:
            return -1
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        elif target > nums[mid]:
            return self.helper(mid+1,right,nums,target)
        else:
            return self.helper(left,mid-1,nums,target)


        