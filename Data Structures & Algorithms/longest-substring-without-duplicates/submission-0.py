class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i am thinking, take a window and maintain a set
        # moment you meet a duplicate shrink the window from left and update the set
        if len(s)==0:
            return 0
        window = set()
        L=0
        lmax = float("-inf")

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L+=1
            window.add(s[R])
            lmax = max(lmax, R-L+1)

        return lmax        