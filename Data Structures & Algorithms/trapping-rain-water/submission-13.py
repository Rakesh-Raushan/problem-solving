class Solution:
    def trap(self, height: List[int]) -> int:
        #water at any index depends on
        # left side support and right side support and on the height at that index
        #infact it depends on left max left to it and right max to right of it
        #infact it depends on the lower of the two
        #we can use two pointers left and right to and maintain left max seen and right max seen and accumulate total

        total_water = 0 #assumption no negative water
        left, right = 0, len(height) - 1
        left_max_h, right_max_h = 0, 0

        while left < right:
            if height[left] <= height[right]:
                total_water += max(0, left_max_h-height[left])
                left_max_h = max(left_max_h, height[left])
                left+=1

            else:
                total_water += max(0, right_max_h-height[right])
                right_max_h = max(right_max_h, height[right])
                right-=1
        
        return total_water
            
            

            


        