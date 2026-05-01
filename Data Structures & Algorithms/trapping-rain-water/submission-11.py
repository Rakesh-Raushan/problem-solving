class Solution:
    def trap(self, height: List[int]) -> int:
        # water trapped at any position depends on
        # max support to its left
        # max support to its right
        # it depends on not immediate left, right but the left max rt max
        # also, the pillar height at i itself reduces the water it can trap
        # so we can say: water_i = min(left_hmax, right_hmax)*1 - h_i but to prevent -ve we do
        # water_i = max(0, min(left_hmax, right_hmax)*1 - h_i)
        # we can take the approach of getting two arrays first in O(1) each to get left_hmax and right_hmax for each i
        # one traversing left to right and other traversing right to left
        # then we can use three arrays, max_left, max_right and curr height arr to calculate total water      

        # left_max, right_max = 0, 0
        # n = len(height)
        # left_max_water, right_max_water = [0]*n, [0]*n
        # for i in range(n):
        #     left_max_water[i] = left_max
        #     right_max_water[n-i-1] = right_max
        #     left_max = max(left_max, height[i])
        #     right_max = max(right_max, height[n-i-1])
        
        # total_water = 0

        # for i in range(n):
        #     total_water+= max(0, min(left_max_water[i],right_max_water[i]) - height[i])
        
        # return total_water

        # but the above O(n) time approach is O(n) in space also
        # we can make this O(1) space using the fact that we are at any index using only the min of the two
        # left_hmax or right_hmax value to calculate the water
        # so if we take an approach of two pointers starting from the two extremes and instead of calculating water left
        # to right for all indexes, we move to calculate water only for the index we know left_hmax matters or right_hmax
        # matters, we can just use the one availabe to us and continue to calculate till l<r moving inward from each side
        # note: when h[l] is lesser than h[r], for this l index, only the lmax matters as rmax will be atleast equal to h[r]
        # which and hence will be the higher one and not needed while the lmax for left is always available as we are moving
        # from left extreme to right and same can be said for case h[r]<h[l]
        l,r = 0, len(height)-1
        lh_max,rh_max = 0, 0
        water = 0
        while(l<r):
            if height[l] < height[r]:
                # we can calculate water at l index and also update lh max and move inwards (rightward)
                water+= max(0, lh_max - height[l])
                lh_max = max(lh_max, height[l])
                l+=1
            else:
                # we can calculate water at r index and also update rh max and move inwards (leftward)
                water+= max(0, rh_max - height[r])
                rh_max = max(rh_max, height[r])
                r-=1
        return water


