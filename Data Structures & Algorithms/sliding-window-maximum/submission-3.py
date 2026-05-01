class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #inputs: nums, k
        from collections import deque

        if k > len(nums):
            return []

        mono_dec_que = deque()

        result = []
        i=0
        while(i<k):
            while mono_dec_que and nums[i] > mono_dec_que[-1]:
                mono_dec_que.pop()
            mono_dec_que.append(nums[i])
            i+=1
        result.append(mono_dec_que[0])
        
        while i<len(nums): 
            if nums[i-k] == mono_dec_que[0]:
                mono_dec_que.popleft()
            
            while mono_dec_que and nums[i] > mono_dec_que[-1]:
                mono_dec_que.pop()
            mono_dec_que.append(nums[i])
            i+=1
            result.append(mono_dec_que[0])
        
        return result




        