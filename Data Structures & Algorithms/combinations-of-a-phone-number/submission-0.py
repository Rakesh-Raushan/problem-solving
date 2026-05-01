class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #234; [[a,b,c],[d,e,f], [g,h,i]]
        #                  a
        #             d    e   f
        #       g   h   i   ghi ghi

        digit_map = {"2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"]}

        results = []
        curr_comb = []

        if not digits:
            return results


        def helper(i):
            #base
            if i==len(digits):
                results.append("".join(curr_comb))
                return

            digit_chars = digit_map[digits[i]]
            for j in range(len(digit_chars)):
                curr_comb.append(digit_chars[j])
                helper(i+1)
                curr_comb.pop()

        helper(0)

        return results
        
        #34, i=0, digit_chars for 3, ["d", "e", "f"]
        # j=0 [d], helper(1)->digits chars of 4 ["g", "h", "i"]
            #j=0 [d,g], helper(2)->BASE add to result and return to 
            #j=1, [d, h],helper(2)->BASE add to result and return to 
            #j=2, [d,i], helper(2)->BASE add to result and return to 
        #j=1 [e], helper(1)

                    