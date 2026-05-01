class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len_str = float('inf')
        for s in strs:
            min_len_str = min(min_len_str, len(s))
        for i in range(min_len_str):
            ch_to_match = strs[0][i]
            for s in strs:
                if s[i] != ch_to_match:
                    return s[:i]
        return s[:min_len_str]