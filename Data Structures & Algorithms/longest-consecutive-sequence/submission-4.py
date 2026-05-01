class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums = [2,20,4,10,3,4,5], if we sort them
        # [2,3,4,5,10,20], sorting is definately one way to do it but will make time O(nlogn)
        # but we see we have three consequetive seq here [2,3,4,5] [10] [20] of lens 4 1 and 1 resp.
        #one thing we can build upon from here is that start of any sequence is the num which for which we do not have
        # left neighbour or say num-1, thus we can simply use this fact to grow unique sequences 
        #since we would need to repeatedly see of we have a left neighbour for a num and also if a right neighbour exists
        # we can maintaina set

        nums_set = set(nums)
        global_streak = 0
        
        for num in nums:
            curr_streak =1
            if num-1 in nums_set:
                #if left neighbour exists, we can't grow the max len consequetive seq form this num, so skip
                continue
            #if not show, grow consequetive sequence starting from this num
            while num+1 in nums_set:
                curr_streak+=1
                num+=1
            #update global streak if curr_streak is longer
            global_streak = max(global_streak, curr_streak)
        
        return global_streak

        #verify [0,3,2,5,4,6,1,1]
        #gs = 0, set (0,1,2,3,4,5,6)
        # num=0, cs=1, -1 not in set so we can grow
            # 1 in set so cs = 2, num=1
            # 2 in set so cs=3, num = 2
            # 3 in set so cs=4, num=3
            # 4 in set so cs = 5, num=4
            # 5 in set so cs = 6, num=5
            # 6 in set so cs =7, num =6
            # 7 not is set
        #gs = max(0,7)=7
        #num=3, 2 in set so skip
        # num=2, 1 in set so skip
        #....
        #0 in set so skip
        #return 7

        
        