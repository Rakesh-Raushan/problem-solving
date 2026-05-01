class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates = [9,2,2,4,6,1,5], target = 8
        #                   []              [9], 
        #          []               [2]
        #     []        [2]     [2]     [2,2]
        #  []. [2]
        #to avoid the duplicates we can skip over them if we sort them
        #sort
        #approach of include exclude as we traverse sorted arr
        #in the exclusion, skip till the num is same
        #sort in place to skip over duplicates
        candidates.sort()
        results = []

        def helper(i, curr_comb, curr_total):
            #case curr total is what we want
            if curr_total == target:
                results.append(curr_comb[:])
                return
            #if curr_total is higher than target, no poin to continue, also no point to continue if i is invalid
            if curr_total > target or i == len(candidates):
                return
            
            #otherwise
            #we want to pursue include curr i ele and exclude it via recursion
            curr_comb.append(candidates[i])
            helper(i+1, curr_comb, curr_total + candidates[i])
            #reset to backtrack
            curr_comb.pop()
            #try exclusion
            #first skip over repeated ele
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            #recurse on exclusion scenario
            helper(i+1, curr_comb, curr_total)

        helper(0,[], 0)
        return results




        