class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #we can solve this in linear time using a monotonically decreasing stack of (temp, temp_idx)

        stack = []
        warmer_temp_days = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            if i>0:
                while stack and temp > stack[-1][0]:
                    #we found a warmer day for stack top, update result and no need to carry this forward in stack
                    stack_temp, stack_temp_idx = stack.pop()
                    warmer_temp_days[stack_temp_idx] = i - stack_temp_idx
            #add this temp
            stack.append((temp,i))
        
        return warmer_temp_days

    #verify [30,38,30,36,35,40,28], stack = [], warmer_temp_days = [0,0,0,0,0,0,0]
    #0,30 > i not > 0, stack = [(30,0)]
    #1,38 > i >0, 38 > stack top 30, st = 30, sti=0, warmer_temp_days = [1,0,0,0,0,0,0], stack = [(38,1)]
    #2,30, 30 not > 38 so stack = [(38,1),(30,2)]
    #3,36 36 >30 so warmer_temp_days = [1,0,1,0,0,0,0] stack = [(38,1), (36,3)]
    #4,35 35. not > 36 so stack = [(38,1), (36,3), (35,4)]
    #5, 40 40>35 so warmer_temp_days = [1,0,1,0,1,0,0], 40>36 so warmer_temp_days = [1,0,1,2,1,0,0], 40>38  
        #so warmer_temp_days = [1,4,1,2,1,0,0] stack =[(40,5)]
    #6,28 28 not > 40 so stack = [(40,5),(28,6)]
    #return [1,4,1,2,1,0,0]
    #edge case if no temp
            

        