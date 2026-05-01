class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.append(j-i)
                    break
                if j == len(temperatures)-1:
                    #last temp but not warmer so append 0
                    result.append(0)
        result.append(0)
        return result

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







        