# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         #case of 2 heights just return the lower height

#         # case more than 2, it should maximize the lower of two and distance bw the two
#         # area = width * height = width * (min(h[i], h[j]))
#         # we can start with max width and then as we move to lower width, we can compare the max_area and update it
#         #  as we move to lower widths we try to play with the lower of the h[i] and h[j] so that they can be increased
#         # because if we keep the lower is same, no matter what happens to higher one, the area will only decrease

#         # two pointer approach can be taken to see water potential at each decreasing w

#         l, r = 0, len(heights)-1
#         w_max = float("-inf")
#         #TODO: check return value for edge case of empty etc

#         while(l<r):
#             if heights[l] < heights[r]:
#                 wp = heights[l] * (r-l)
#                 if wp > w_max:
#                     w_max = wp
#                 l+=1
#             else:
#                 wp = heights[r] * (r-l)
#                 if wp > w_max:
#                     w_max = wp
#                 r-=1
        
#         return w_max

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i ,j = 0, len(heights) - 1

        max_water = 0

        while(i<j):
            curr_water = (j-i)*min(heights[i], heights[j])
            max_water = max(curr_water, max_water)
            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1
        
        return max_water

#verification
#height = [1,7,2,5,4,7,3,6]
#i=0,j=8-1=7, max_water = 0
#1<7: curr_water = (7-1)*1 = 6, max_water=6, i+=1
#i=1,j=7,1<7, curr_water=6*6=36, max_water =36, j=6
#1<6, curr_water = 5*3=15, max_water =36, j=5
#1<5, curr_water = 4*7=28, max_water =36, i=2
#2<5, curr_water = 3*2=6, max_water =36, i=3
#3<5,  curr_water = 2*5=10, max_water =36, i=4
#4<5, curr_water = 1*4=4, max_water =36, i=5
#5<5 false

        