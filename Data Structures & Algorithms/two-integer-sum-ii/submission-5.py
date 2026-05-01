# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
#         l=0
#         r=len(numbers)-1

#         while(l<r):
#             if numbers[l] + numbers[r] > target:
#                 r-=1
#             elif numbers[l] + numbers[r] < target:
#                 l+=1
#             else:
#                 return [l+1,r+1]
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        while(i<j):
            if numbers[i] + numbers[j] ==target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
        
