class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #idea is that we will have n open and n closed brackets but we can always add an open bracket if we have left
        #but for the closed we can only add only if num of closed brackets is less than open
        #so we can build a recursive solution on this idea where we recursively add brackets to reach 2n size
        #as per the above logic and keep accumulating them

        result = []

        def add_bracket(curr_state: str, count_open: int, count_closed: int) -> None:
            if len(curr_state) == 2*n:
                result.append(curr_state)
            
            #else add brackets

            #add open bracket branch
            if count_open < n:
                #recurse after adding an open bracket
                add_bracket(curr_state + "(", count_open + 1, count_closed)
            
            #add closed bracket branch
            if count_closed < n and count_closed < count_open:
                #recurse after adding a closed bracket
                add_bracket(curr_state + ")", count_open, count_closed + 1)
        
        add_bracket("", 0, 0)
        return result
