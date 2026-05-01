class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        slow = fast = 0

        while slow+1 < len(nums):
            if nums[slow] == nums[slow+1]:
                return nums[slow]
            slow = slow+1
        
        while fast+2 < len(nums):
            if nums[fast] == nums[fast+2]:
                return nums[fast]
            fast = fast+2
        
        return nums[0]