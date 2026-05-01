class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # p1, p2, p3, min eating rate k, total sum=h
        # any pile p<k 1 hour, p>k p//k +1, eating rate 1, 2, 3 or say upto
        # i start with k 1, if not poss then 2, if not then 4, if not then 8
        # if yes other than k =1, change the search space to 4 to 8 kind

        def can_eat(k,h):
            t=0
            for p in piles:
                if p<=k:
                    t+=1
                else:
                    t+=((p//k)+1)
            return t<=h
        
        k=1
        while not can_eat(k,h):
            k*=2
        if k==1 or not can_eat(k-1,h):
            return k
        else:
            l, r =k//2, k
            while (l<=r and l>0):
                m = (l+r)//2
                if can_eat(m,h):
                    if not can_eat(m-1,h):
                        return m
                    else:
                        r=m-1
                else:
                    l=m+1
        return -1
        


        