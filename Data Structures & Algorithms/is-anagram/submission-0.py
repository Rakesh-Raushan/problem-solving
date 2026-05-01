class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        from collections import Counter
        s_counts = Counter(s)

        for char in t:
            if char not in s_counts or s_counts[char]==0:
                return False
            else:
                s_counts[char]-=1
        
        return True
        