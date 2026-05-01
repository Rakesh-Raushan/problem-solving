class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # i,j=0,0
        # l = len(nums)
        # ans = [0]*l*2
        # while i < 2*l:
        #     while j < l:
        #         ans[i] = nums[j]
        #         j+=1
        #         i+=1
        #     j=0
        return nums*2#ans
# [1,4,1,2,1,4,1,2]




# brute: [1,4,1,2]
# len=4, so i take [0]*8 = [0,0,0,0,0,0,0,0]
# i,j=0, 
# while i<8:
#   while j<4:
#       new[i] = old[j]
#       j+=1
#       i+=1
#   j=0
# this is O(n) and space O(n)


        