class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r =0, 0
        seen = set()
        max_window_len = 0
        while r < len(s):
            if s[r] not in seen:
                #expand the window by 1 from right
                seen.add(s[r])
                r+=1
                max_window_len = max(max_window_len, r-l)
            else:
                #shrink the window by 1 from left
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
        return max_window_len

#verify s = "zxyzxyz", seen = {}
#l 0 r 0, mwl = 0, 0 < 7, s[0]= z not in seen, seen = {z,},  r=1, mwl = 0,
#l 0, r 1, 1<7 s[1] x not in seen so seen = {z,x}, r=2, mwl = 2
#l 0, r 2, 2<7 s[2] y not in seen so seen = {z,x,y} r=3, mwl = 3
#l0, r3 3<7 s[3] z in seen so shrink seen = {x, y}, l=1, mwl = 3
#l1 r3 3<7 s[3] z not in seen so seen = {x,y,z}, r=4, mwl = 3
#l1 r4, 4<7 x in seen so seen = {y,z} l=2, mwl = 3
#l2, r4, y in seen so seen = {z}, 
#
        