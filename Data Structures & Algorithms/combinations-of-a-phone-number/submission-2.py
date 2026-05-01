class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #so at every digit i have mutliple options to explore and i need to accumulate all
        #possibilities, so clearly signifies using backtracking
        if len(digits)==0:
            return []
        n = len(digits)

        digit_letter_map = {"2" : ["a", "b", "c"],
                            "3" : ["d", "e", "f"],
                            "4" : ["g", "h", "i"],
                            "5" : ["j", "k", "l"],
                            "6" : ["m", "n", "o"],
                            "7" : ["p", "q", "r", "s"],
                            "8" : ["t", "u", "v"],
                            "9" : ["w", "x", "y", "z"]}
        
        #we will defina recursive helper to explore the possible mapping
        #as we traverse the digits starting from 1st position
        letter_combinations = []
        def helper(idx, curr_str):
            nonlocal letter_combinations
            #if last index, means we have explored till end
            if idx == n:
                #append this to our letter_combinations
                letter_combinations.append(curr_str)
                return
            
            for letter in digit_letter_map[digits[idx]]:
                helper(idx+1, curr_str + letter)
        
        helper(0,"")
        return letter_combinations

    #verify: "34" > 
    #helper(0,""), ["d", "e", "f"], 
                    # helper(1,"d") ["g", "h", "i"]
                                    #helper(2,"dg") idx=n so add to result "dg"
                                    #helper(2,"dh"), same
                                    #helper(2,"di"), same
                    # helper(1,"e") ["g", "h", "i"]
                                    #helper(2,"eg") idx=n so add to result "eg"
                                    #helper(2,"eh"), same
                                    #helper(2,"ei"), same
                    # helper(1,"f") ["g", "h", "i"]
                                    #helper(2,"fg") idx=n so add to result "fg"
                                    #helper(2,"fh"), same
                                    #helper(2,"fi"), same
                    

        