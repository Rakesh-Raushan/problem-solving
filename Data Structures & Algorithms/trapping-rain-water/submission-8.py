class Solution:
    def trap(self, height: List[int]) -> int:
        # water trapped at any position depends on
        # support to its left
        # support to its right
        # example at index 1, left 2, right 3, water 2
        # example at index 3, left 3 but right 0, still water 2
        # it depends on not immediate left, right but the left max rt max
        # also, the pillar height at i itself reduces the water it can trap
        # example at index 3, if its height was 0, it would have hold 3 not 2
        # so we can say: water_i = min(left_hmax, right_hmax)*1 - h_i
        # check this for boundary, i=8, right max =0, 0-1, -1 but water 0
        # okay so can't go negative, so: water_i = max(0, min(left_hmax, right_hmax)*1 - h_i)

        # to code this since we need left and right both information
        # we can take 2 pointers at left and right starting

        l,r = 0, len(height)-1
        lh_max,rh_max = 0, 0
        water = 0
        # [4,2,3] - 
        # >> l=0,r=2,lhmax=0, rhmax=0,w=0, else,
        while(l<r):
            #moving from two ends we can add the water
            #check which one is lower, left or right
            if height[l] < height[r]:
                if lh_max < height[l]:
                    lh_max = height[l]
                water+= lh_max - height[l]
                print(lh_max, height[l])
                l+=1
            else:
                if rh_max < height[r]:
                    rh_max = height[r]
                water+= rh_max - height[r]
                print(rh_max, height[r])
                r-=1
        return water


