class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #one brute force kind of approach can be to see how big a rectangle can be made
        #using the curr height by expanding left and right from each and update global max
        max_area = 0
        for i in range(len(heights)):
            curr_height = heights[i]
            j=i+1
            k=i-1
            curr_area = curr_height
            #grow right
            while j < len(heights) and curr_height<=heights[j]:
                curr_area+=curr_height
                j+=1
            while k >=0 and curr_height<=heights[k]:
                curr_area+=curr_height
                k-=1
            max_area = max(curr_area, max_area)
        
        return max_area

        #verify [1,3,7], len=3
        #i=0, ma = 0, ch=1,j=1, ca = 1, 1<3 and 1<3, ca=1+1=2,j=2<3 and 1<7, ca=3 ma = max(3,0)=3
        #i=1, ma = 3, ch=3,j=2, ca=3, 2<3 and 3<7, ca = 3+3,j=3not less than 3, ma = max(6,3) = 6
        #i=2, ma=6, ch=7, j=3, ca=7, 3<3 not true so ma = max(7,6)=7 works!
        #verify [7,1,7,2,2,4], len=6
        #i=0, ma=0, ch=7, j=1, ca=ch=7while fails, ma=max(0,7)=7
        #i=1, ma=7, ch=1,j=2, ca=ch=1 ca=2,ca=3,4,5,ma=7
        #i=2, ma=7,ch=7,j=3,ca=7,ma=7
        #i=3, ma=7, ch=2,ca=2,ca=4,ma
        