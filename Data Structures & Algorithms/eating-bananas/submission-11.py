class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # import math
        k_min, k_max = 1, max(piles)
        while(k_min<k_max) :   
            k_mid = (k_min+k_max)//2
            # t_k_mid = sum([math.ceil(p/k_mid) for p in piles]) math ceil requires import and is slower
            #faster option is this integer div
            t_k_mid = sum([((p+k_mid-1)//k_mid) for p in piles])
            if t_k_mid <=h:
                #it means a smaller rate also exists so 
                k_max=k_mid
            else:
                #we can only look for rates higher than k_mid
                k_min = k_mid + 1
        
        return k_min
    #verify: piles = [1,4,3,2], h = 9
    #k_min = 1, k_max = 4
    #1<4, k_mid = 2, tkmid = 1+2+2+1=6 <9
    #k_min = 1,k_max=2
    #1<2, k_mid = 1, tkmid = 1+4+3+2 = 10>9
    #k_min=2,k_max = 2
    #break k_min=2
    #case: piles = [25,10,23,4], h = 4
    #k_min = 1, k_max = 25
    #1<25, k_mid = 13, tkmid = 2+1+2+1=6 >4
    #kmin = 14, kmax=25, kmid=19,tkmid=2+1+2+1 >4
    #kmin = 20, kmax=25, kmid=22, tkmid = 2+1+2+1>4
    #kmin=23, kmax=25, kmid = 24, tkmid = 5>4
    #kmin=25, kmax=25, kmid=25, tkmid = 4=4
    #kmax=25
        