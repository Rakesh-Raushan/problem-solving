class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #since amount of water. = height supported * width
        #for max we can start with max width and keep on decreasing it
        #also the height actually depends on the lower of the two heights
        max_water = 0

        if len(heights) <2:
            return max_water

        left, right = 0, len(heights)-1

        while left < right:
            curr_capacity = min(heights[left], heights[right]) * (right-left)
            max_water = max(max_water, curr_capacity)
            if heights[left] <= heights[right]:
                #left one is smaller and deciding one
                left+=1
            else:
                right-=1
        
        return max_water
    
    #verify: height = [1,7,2,5,4,7,3,6]
    #l=0,r=7, mw=0
    #0<7, cc= min of 1,6 * 7=7, so mw=7, h[l]<h[r] so l=1
    #1<7 cc= min of 7 and 6 so 6, 6*6=36, mw=36, h[l]>h[r], so r=6
    #1<6 cc= min of 7 and 3 so 3*5=15, mw=36, h[l]>h[r] so r=5
    #1,5 cc= min of 7,7 so 7*4, cc=28, mw=36, h[l]=h[r] so l=2
    #2<5 cc=min of 2 and 7 so 2, cc=2*3=6, mw=36, h[l]<h[r] so l=3
    #3<5, cc = min 5 and 7 so 5*2=10, mw=36, h[l]<h[r] so l =4
    #4<5 cc = min 4 and 7 so 4*1=4, mw=36, h[l]<h[r] so l = 5
    #5 not <5 so end, mw=36 ans