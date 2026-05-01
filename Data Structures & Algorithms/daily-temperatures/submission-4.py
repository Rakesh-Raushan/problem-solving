class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     result = []
    #     for i in range(len(temperatures)):
    #         for j in range(i+1, len(temperatures)):
    #             if temperatures[j] > temperatures[i]:
    #                 result.append(j-i)
    #                 break
    #             if j == len(temperatures)-1:
    #                 #last temp but not warmer so append 0
    #                 result.append(0)
    #     result.append(0)
    #     return result

#verfy: Input: temperatures = [30,38,30,36,35,40,28]
# result = [], len = 7 i(0,6)
#i=0, j=1, result [1]
#i=1, j =2, 2!=7, j=3, 3!=7, j=4, j=5, result[1,4]

# Input: temperatures = [22,21,20]
# result = [], len = 3 i(0,2)
#i=0, j=1, result []
#i=0, j=2, [0]
#i=1, j=2, [0,0]
#i=2, j=3??
    
    #above solution works but is O(n^2), we can use a monotonic stack to track temperatures we go across
    #and use that to get results in a linear time O(n)
    #we maintain a monotonically decreasing stack of temperatures as we traverse the temperatures array
    #if we curr_temp is greater than the top of the stack, it mean for the top of stack temp index, we have result based on curr
    #so we pop and update result (we keep indexes also along with temp on the stack)

    #sol
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = [] #to maitain (temp,temp_idx)

        #traverse and update stack and results
        for curr_idx, curr_temp in enumerate(temperatures):
            #check if we came across a warmer day, just by comparing with the top we can be sure
            #since we are maintaining, monotonically decreasing arr, if curr day is not warmer for top then it can't
            #be warmer for any other as they must be of higher val
            while stack and curr_temp > stack[-1][0]:
                #warmer so pop it, as we can fulfil the result for this day and no need to maintain it any further in stack
                top_temp, top_idx = stack.pop()
                #update result for this day as we got a warmer one for this
                result[top_idx] = curr_idx - top_idx
            #push the curr day temp and idx on stack to track them for warmer days we will meet
            stack.append((curr_temp, curr_idx))
        
        return result

    #verify with [30,38,30,39] ans = [1,2,1,0]
    #n = 4, result [ 0,0,0,0], stack = []
    #0,30, stack = [(30,0)]
    #1,38, 38>30, result[0] = 1-0=1 so result= [1,0,0,0], stack = [(38,1)]
    #2,30, 30>38 no so push, stack = [(38,1), (30,2)]
    #3,39, 39>30, so pop result[2] = 3-2=1, result = [1,0,1,0], stack=[(38,1)]
    #   also 39>38, so pop result[1] = 3-1 =2, result[1,2,1,0]
    #push stack [(39,3)], out of loop, works!







        