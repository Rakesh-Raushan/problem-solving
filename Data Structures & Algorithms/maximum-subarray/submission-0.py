class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum+=num

            if cur_sum > max_sum:
                max_sum = cur_sum
        
        return max_sum

        #      [2,-3,4,-2,2,1,-1,4]
        # cur.  2  -1 4 2 4 5 4 8
        # max.  2.  2 4 4 4 5 5 8

        