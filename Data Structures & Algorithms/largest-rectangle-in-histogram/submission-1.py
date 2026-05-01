class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # max_area = 0
        # for i in range(len(heights)):
        #     curr_height = heights[i]
        #     j=i+1
        #     k=i-1
        #     curr_area = curr_height
        #     #expand right
        #     while j < len(heights) and curr_height<=heights[j]:
        #         curr_area+=curr_height
        #         j+=1
        #     #expand left
        #     while k >=0 and curr_height<=heights[k]:
        #         curr_area+=curr_height
        #         k-=1
        #     max_area = max(curr_area, max_area)
        
        # return max_area

        #above is a O(n^2) sol but we can see that for every ele we need the dist we can expand to rt and left
        #if we can get left and right dist for each in O(n), we can get max in O(1)
        # we also see max exp to left or right depends on dist to smaller ele than curr to right and left
        # we know we can achieve this next smaller, next larger kind of thing in O(n) with monotonic stacks
        # so let's use that

        stack = [] #make a monotonic increasing stack as we need next smaller ele so top will have largest
        next_smaller_ele_dist = [0]*len(heights)
        #calculate dist to next smaller ele for each
        for curr_idx, curr_height in enumerate(heights):
            while stack and curr_height<stack[-1][0]:
                #to ensure increasing stack, pop 
                #also, it means curr_height is the next smaller height for for popped index
                pop_h, pop_idx = stack.pop()
                next_smaller_ele_dist[pop_idx] = curr_idx - pop_idx - 1
            #after popping all larger push the curr h and curr idx for finding their next smaller ele dist
            stack.append((curr_height, curr_idx))
        #check if there are still elements in the stack, if so calculate their distance as per current idx
        curr_idx+=1 #increment to handle boundary i
        while stack:
            pop_h, pop_idx = stack.pop()
            next_smaller_ele_dist[pop_idx] = curr_idx - pop_idx - 1
        #at this point we have next_smaller_ele_dist for all ele

        # we can do the exact thing on reversed array of heights to get the prev smaller ele dist for all
        # in reversed order
        stack = [] #make a monotonic increasing stack as we need next smaller ele so top will have largest
        prev_smaller_ele_dist = [0]*len(heights)
        #calculate dist to next smaller ele for each
        rev_heights = heights[::-1]
        for curr_idx, curr_height in enumerate(rev_heights):
            while stack and curr_height<stack[-1][0]:
                #to ensure increasing stack, pop 
                #also, it means curr_height is the next smaller height for for popped index
                pop_h, pop_idx = stack.pop()
                prev_smaller_ele_dist[pop_idx] = curr_idx - pop_idx - 1
            #after popping all larger push the curr h and curr idx for finding their next smaller ele dist
            stack.append((curr_height, curr_idx))
        #check if there are still elements in the stack, if so calculate their distance as per current idx
        curr_idx+=1 #increment to handle boundary i
        while stack:
            pop_h, pop_idx = stack.pop()
            prev_smaller_ele_dist[pop_idx] = curr_idx - pop_idx - 1
        #reverse it to suit our need
        prev_smaller_ele_dist = prev_smaller_ele_dist[::-1]
        #at this point we have prev_smaller_ele_dist for all ele in right order

        #final max area at each i can now be easily calculated as 
        #height[i]*(1+prev_smaller_dist+next_smaller_dist)
        max_area_at_idx = [h*(1+p+n) for h,p,n in zip(heights,prev_smaller_ele_dist, next_smaller_ele_dist)]

        return max(max_area_at_idx)
