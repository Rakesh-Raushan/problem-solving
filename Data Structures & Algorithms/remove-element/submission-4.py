class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0,0
        while j < len(nums):
            if nums[j] == val:
                j+=1
            else:
                nums[i] = nums[j]
                i+=1
                j+=1
        return i

#nums = [1,1,2,3,4], val = 1
#i 0, j 0
#0<5
#nums[j] == val, j=1
#1<5
#nums[j] == val, j=2
#2<5
#nums[j] != val, i<j, nums[0] = 2, [2,1,2,3,4], i=1,j=3
#3<5
#nums[j] != val, i<j, nums[1] = 3, [2,3,2,3,4],i=2,j=4
#4<5
#nums[j] != val, i<j, nums[2] = 4, [2,3,4,3,4], i=3,j=5

        