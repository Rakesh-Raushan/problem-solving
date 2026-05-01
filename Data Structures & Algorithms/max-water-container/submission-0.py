class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #case of 2 heights just return the lower height

        # case more than 2, it should maximize the lower of two and distance bw the two
        # area = width * height = width * (min(h[i], h[j]))
        # we can start with max width and then as we move to lower width, we can compare the max_area and update it
        #  as we move to lower widths we try to play with the lower of the h[i] and h[j] so that they can be increased
        # because if we keep the lower is same, no matter what happens to higher one, the area will only decrease

        l, r = 0, len(heights)-1

        max_area = float("-inf")

        while(l<r):
            w = r-l
            h_min = min(heights[l], heights[r])
            max_area = max(max_area, w*h_min) #7*1, 6*6, 5*3, 4*7, 3*2,2*5
            if heights[l] <= heights[r]:
                l+=1 # 1
            else:
                r-=1 #6
        
        return max_area


        