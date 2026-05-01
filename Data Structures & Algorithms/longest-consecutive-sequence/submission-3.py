
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_set = set(nums)
#         longest_streak = 0

#         for n in nums:
#             if n-1 in nums_set:
#                 continue
#             else:
#                 curr_num = n
#                 curr_streak = 1
#                 while curr_num+1 in nums_set:
#                     curr_num = curr_num+1
#                     curr_streak+= 1
#                 longest_streak = max(longest_streak, curr_streak)
        
#         return longest_streak
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        overall_streak = 1

        for num in nums_set:
            curr_streak = 1
            if num-1 in nums_set:
                continue
            else:
                while(num+1 in nums_set):
                    curr_streak+=1
                    num = num+1
                overall_streak = max(curr_streak, overall_streak)
        
        return overall_streak
