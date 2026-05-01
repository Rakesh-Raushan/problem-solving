class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Input is nums - distinct int; target
        #unique combs summing to target, any numbr can be choosen any number of times
        #nums = [2,5,6,9] , target = 9
        # [2][2,2],[2,2,2], [2,2,2,2]
        # [2,5],[2,2,5]
        #has map of max freq of each
        #{2:4, 5:1,6:1,9:1}
        #for every key generate the subsets
        #2->           [],                [2],               [2,2] ,                   [2,2,2],                                  [2,2,2,2]
        #5->       [],     [5],        [2],    [2,5],           [2,2] [2,2,5],             [2,2,2]                                    [2,2,2,2]
        #6->     [] [6]    [5]       [2,6]     [2,5]           [2,2]. [2,2,5]              [2,2,2]                                 [2,2,2,2]
        #9->

        #iterative approach can be

        # results = []
        # collect_subs_to_carry = [[]]
        # curr_subs = [[]]

        # for num in nums:
        #     # curr_subs = collect_subs_to_carry[:]
        #     collect_subs_to_carry = []
        #     for sub in curr_subs:
        #         diff = target
        #         for num_rep in range(diff//num+1):
        #             sub_copy = sub[:]
        #             sub_copy.extend([num]*num_rep)
        #             #if sum is target add to results
        #             if sum(sub_copy) ==target:
        #                 results.append(sub_copy)
        #             elif sum(sub_copy) < target:
        #                 #carry them forward for next num
        #                 collect_subs_to_carry.append(sub_copy)
        #     curr_subs = collect_subs_to_carry[:]
        
        # return results

        #let's look at backtracking approach as well

        results = []

        def dfs(idx, curr_sub_and_sum):
            #base case
            curr_sub, curr_sub_sum = curr_sub_and_sum
            if idx==len(nums) or curr_sub_sum >= target:
                if curr_sub_sum == target:
                    results.append(curr_sub[:]) #must take a copy
                return
            
            diff = target - curr_sub_sum

            for count in range(diff//nums[idx]+1):
                new_sub = curr_sub + [nums[idx]]*count
                new_sub_sum = curr_sub_sum + nums[idx]*count
                #then recurse on new one
                dfs(idx+1, (new_sub, new_sub_sum))
        
        dfs(0,([],0))

        return results

                    

