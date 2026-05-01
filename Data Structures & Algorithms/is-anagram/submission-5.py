class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            map_s = {}
            for ch in s:
                if ch in map_s:
                    map_s[ch]+=1
                else:
                    map_s[ch]=1
            map_t = {}
            for ch in t:
                if ch in map_t:
                    map_t[ch]+=1
                else:
                    map_t[ch]=1

            return map_s == map_t
        return False