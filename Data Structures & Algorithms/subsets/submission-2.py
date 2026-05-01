class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Input: nums - unique ints ; Exp Ans: All possible subsets of nums
        #ex [1,2,3],           []
        #           []                      [1]
        #      []       [2]           [1]       [1,2]
        #   []  [3]   [2]  [2,3]   [1]  [1,3] [1,2]   [1,2,3] 
        #above are the 2^n subsets possible
        #we can collect result only when backtracking

        # subsets_list = [[]]
        # from copy import copy
        # for num in nums:
        #     #i have two resulting choices
        #     curr_subsets_list = subsets_list[:] #acopy
        #     for sub in curr_subsets_list:
        #         sub_copy = copy(sub)
        #         sub_copy.append(num)
        #         subsets_list.append(sub_copy)

        # return subsets_list

        #[1,2,3] and [[]]
        #1, sub [], sub_with_num = [1]; [[],[1]]
        #2 sub [], sub_with_num = [2]. [[], [1],[2]]
          # sub [1], sub_with_num = [1,2], [[], [1],[2], [1,2]]

        #above is a solution without backtracking and has O(n2) time complexity
        # let's write backtracking also, where we collect the subsets at the end of dfs

        results = []
        n = len(nums)

        def dfs(idx, curr_set):
            if idx ==n:
                results.append(curr_set[:])
                #append a copy to result and return
                return
            
            #include it and recurse on it
            curr_set.append(nums[idx])
            dfs(idx+1, curr_set)
            curr_set.pop()
            #not include and recurse on it
            dfs(idx+1, curr_set)

        dfs(0,[])
        return results

        #[1,2,3]
        #n=3, results = []
        #call(0,[])
        #0!=3 -> [1]
            #call(1,[1])
            #1!=3, [1,2]
                #call(2,[1,2])
                #2!=3, [1,2,3]
                    #call(3,[1,2,3])
                    #3==3; results [[1,2,3]] back to call(2,[1,2])
                #call(2,[1,2])
                #pop [1,2],
                    #call(3,[1,2])
                    #3==3; results [[1,2,3], [1,2]] back to call (2,[1,2])
                #call(2,[1,2])
                #pop [1]
                    #call(3, [1])
                    #3==3, results [[1,2,3], [1,2], [1]] back to call call(1,[1])
            #call(1,[1])
                #pop []
                    #call(3,)







        