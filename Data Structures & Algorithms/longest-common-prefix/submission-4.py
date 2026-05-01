class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     min_len_str = float('inf')
    #     for s in strs:
    #         min_len_str = min(min_len_str, len(s))
    #     for i in range(min_len_str):
    #         ch_to_match = strs[0][i]
    #         for s in strs:
    #             if s[i] != ch_to_match:
    #                 return s[:i]
    #     return s[:min_len_str]
    #brute force, takes O(n*m) time and O(1) space as we are not using any extra space, neither efficient nor elegant 
    #but actually this is the optimum solution
    #one elegant not exactly best sol is to sort all the strings and then just get the common part in 1st and last str
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sorted_strs = sorted(strs)
        first_str, last_str = sorted_strs[0], sorted_strs[-1]

        for i in range(len(first_str)):
            if first_str[i] != last_str[i]:
                return first_str[:i]
        return first_str
    #this one is not as optimal as the first one for long strings because sorting is nlogn and we do it for all strings say if avg size is m
    #total time m*nlogn, so this approach is m*nlogn but earlier one was m*n , logn term becomes large for long lists (like comparing O(n) vs O(nlogn))

        
