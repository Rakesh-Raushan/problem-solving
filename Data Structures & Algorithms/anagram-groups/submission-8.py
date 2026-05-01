class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first let's brute force it by comparing every string with every other, n(n-1)/2 pairs
        res = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            res[sorted_s].append(s)
        
        return list(res.values())

