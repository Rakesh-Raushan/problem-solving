class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        count_map = {'open':0, 'closed': 0}
        self.helper([], count_map, results, n)
        results_str = ["".join(exp_list) for exp_list in results]
        return results_str

    def helper(self, curr_exp, count_map, results, n):
        #base case, add the exp to results
        if len(curr_exp) == 2*n:
            results.append(curr_exp[:])
            return
        
        # check if we have open brackets left
        if count_map['open'] < n:
            #we can add open brackets
            curr_exp.append('(')
            #update the count_map
            count_map['open']+=1
            #build of this curr_exp
            self.helper(curr_exp, count_map, results, n)
            # reset to backtrack
            curr_exp.pop()
            count_map['open']-=1
        
        #check if we have closed brackets lesser than open
        if count_map['closed'] < n and count_map['closed'] < count_map['open']:
            #we can add closed bracket to expression
            curr_exp.append(')')
            #update the count_map
            count_map['closed']+=1
            #build of this curr_exp
            self.helper(curr_exp, count_map, results, n)
            # reset to backtrack
            curr_exp.pop()
            count_map['closed']-=1
        

        