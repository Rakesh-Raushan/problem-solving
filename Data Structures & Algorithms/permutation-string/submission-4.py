class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #input: s1 and s2 #output: true or false
        #i am thinking i can just traverse s2 with a window len of s1 and look for a matching window
        # to do that, one pointer is enough as window is fixed
        # for comparision i can use a helper function that traverses linearly to ensure it is permutation or not
        # we can get a O(n*m) solution way and space O(m)
        from collections import Counter
        n = len(s1)
        counter_s1 = Counter(s1)
        i=n
        while(i<=len(s2)):
            counter_s2 = Counter(s2[i-n: i])
            if counter_s2==counter_s1:
                return True
            i+=1
            
        return False


        

            