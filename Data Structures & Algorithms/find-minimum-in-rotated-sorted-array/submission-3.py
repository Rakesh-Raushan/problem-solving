class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left, right = 0, len(nums)-1

        while(left <= right):
            mid = (left + right)//2
            #check cond
            #boundary cond
            if (mid==0 and nums[mid]<nums[mid+1]) or (mid==len(nums)-1 and nums[mid]<nums[mid-1]) or (nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]):
                return nums[mid]
            elif nums[mid] < nums[mid+1] and nums[mid] < nums[right]:
                right = mid-1
            else:
                left = mid+1

            
#verify:
#Input: nums = [3,4,5,6,1,2]
# l=0, r=5 -> 0<5; m=2, nums[m] = 5<6 and 5>2 left=mid+1
#l=3, r=5, m=4, nums[m] = 1, returned
#Input:  nums = [4,5,0,1,2,3]
# l=0, r=5; 0<5, m=2, 
#input nums = [4,5,6,7], 
#l=0, r=3, m =1, r=2
#l=0,r=2, m=1,r=1
#l=0,r=1,m=0,