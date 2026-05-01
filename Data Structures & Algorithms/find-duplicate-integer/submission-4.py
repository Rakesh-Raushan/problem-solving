class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0
        
        # Detect cycle (with special handling for first comparison)
        first_iteration = True
        while slow != fast or first_iteration:
            first_iteration = False
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # Find cycle entry (duplicate number)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        



        