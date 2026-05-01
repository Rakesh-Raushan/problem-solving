class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while(left <= right):
            #calculate the mid index for this array
            mid = (left+right)//2
            #compare to target
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        
        return -1

    #verify
    #case1
    #nums = [-1,0,2,4,6,8], target = 4
    #l=0, r= 6, m = 3, target=4 num[m]=4, target==mid so ans=3
    #Input: nums = [-1,0,2,4,6,8], target = -1
    #l=0,r=6,m=3,num[m]=4, target=-1 <m so r=2
    #l=0, r=2, m=1, num=0, target<num so r=0


        