class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                count+=1
            else:
                if count > max_length:
                    max_length = count
                count = 0
        if count > max_length:
            max_length = count
        return max_length
        