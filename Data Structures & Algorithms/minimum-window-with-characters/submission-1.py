class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #input: s, t
        #output, shortest substring of s, if not possible them """

        #start l=0
        #iterate on r=0 to len(s)
        # while r< len(s) and counter_t, if s[r] in t, reduce it and for zero remove it
        # if counter_t return ""
        # else: get curr_len and update max
        from collections import Counter
        left = 0
        right = 0
        min_len = float("inf")

        while right<len(s):
            counter_t = Counter(t)
            if s[right] not in counter_t:
                right+=1
                left+=1
                continue
            while right<len(s) and counter_t:
                if s[right] in counter_t:
                    #update the counter
                    counter_t[s[right]] = counter_t[s[right]] - 1
                    #check if update made its val zero
                    #if val became zero remove the entry itself from dict so that s[right] in counter_t does not give false pos
                    if counter_t[s[right]] == 0:
                        del counter_t[s[right]]
                    #check if the whole dict is done
                    if not counter_t:
                        #check if this is a better min len sub
                        if right+1-left < min_len:
                            min_len = right+1-left
                            min_sub = s[left:right+1]
                        break
                right+=1
            #start fresh with left and right both at the next
            left+=1
            right=left
        
        return min_sub if min_len != float("inf") else ""
            



        