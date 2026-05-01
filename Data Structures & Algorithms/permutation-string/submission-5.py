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

        #this solution is O(n*m) m-len(s1), n-len(s2) but we can make it O(n) by not calculating counter s2[sub] 
        #each time and rather updating the existing counter by reducing count of moved over and incresing count of moved
        #onto char, but note, also do del counter_s2[moved from char] if its count becomes zero, so that we can still compare
        #counter_s1 == counter_s2, else the zero count keys can create issues


        

            