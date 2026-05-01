class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     else:
    #         return sorted(s) == sorted(t)
    # O(nlogn + mlogm) in time since sorted is loglinear in python (timsort)
    # O(1) in space

    #other solution is to use hashmap
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            char_map = {}
            for i in range(len(s)):
                char_map[s[i]] = char_map.get(s[i],0) + 1
                char_map[t[i]] = char_map.get(t[i],0) - 1
            
            for ch in char_map:
                if char_map[ch] != 0:
                    return False
            return True

