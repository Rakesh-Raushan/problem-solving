class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #case of 2 heights just return the lower height

        # case more than 2, it should maximize the lower of two and distance bw the two
        # area = width * height = width * (min(h[i], h[j]))
        # we can start with max width and then as we move to lower width, we can compare the max_area and update it
        #  as we move to lower widths we try to play with the lower of the h[i] and h[j] so that they can be increased
        # because if we keep the lower is same, no matter what happens to higher one, the area will only decrease

        # two pointer approach can be taken to see water potential at each decreasing w

        l, r = 0, len(heights)-1
        w_max = float("-inf")
        #TODO: check return value for edge case of empty etc

        while(l<r):
            if heights[l] < heights[r]:
                wp = heights[l] * (r-l)
                if wp > w_max:
                    w_max = wp
                l+=1
            else:
                wp = heights[r] * (r-l)
                if wp > w_max:
                    w_max = wp
                r-=1
        
        return w_max
            


        