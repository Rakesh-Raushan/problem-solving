class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Input: nums - unique ints ; Exp Ans: All possible subsets of nums
        #ex [1,2,3],           []
        #           []                      [1]
        #      []       [2]           [1]       [1,2]
        #   []  [3]   [2]  [2,3]   [1]  [1,3] [1,2]   [1,2,3] 
        #above are the 2^n subsets possible
        #we can collect result only when backtracking

        subsets_list = [[]]
        from copy import copy
        for num in nums:
            #i have two resulting choices
            curr_subsets_list = subsets_list[:] #acopy
            for sub in curr_subsets_list:
                sub_copy = copy(sub)
                sub_copy.append(num)
                subsets_list.append(sub_copy)

        return subsets_list

        #[1,2,3] and [[]]
        #1, sub [], sub_with_num = [1]; [[],[1]]
        #2 sub [], sub_with_num = [2]. [[], [1],[2]]
          # sub [1], sub_with_num = [1,2], [[], [1],[2], [1,2]]

        