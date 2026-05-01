class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # so essentially, I need to find the longest substring with say upto k+1 distinct char
        # the crux lies in the fact that any window will be valid if window length - (count of most freq char) <=k
        # so we need to maintain the count of chars

        count = {}
        l=0
        max_len = 0
        # maxf = 0
        for r in range(len(s)):
            # let's increment every char we see as we iterate through the string
            count[s[r]] = 1 + count.get(s[r], 0)
            # maxf = max(maxf, count[s[r]])

            # we also need to ensure curr window s[l,r+1],does not break the threshold
            # or say while it breaks we will update count and shorten the window from left
            while(r-l+1 - max(count.values())>k):
                count[s[l]] = count.get(s[l]) - 1
                l+=1

            # we would also update max len everytime by comparing it to old max and cur window len
            # which we ensured is valid by putting the while check before it
            max_len = max(max_len, r-l+1)

        return max_len

        # in the above code, we can further ensure that we get strict O(n) instead of O(26n)
        # by replacing max(count.values()) with maxf
        # reason why an ever increasing maxf works is that the check while(r-l+1 - max(count.values())>k)
        # or while(r-l+1 - maxf)>k)
        # changes only if maxf increases or r-l+1 decreases, since r-l+1 will decrease and maxf increase happens
        # a decreasing of maxf is not needed and code works


        
        