class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #first sort the nums so that we can avoid duplicates
        nums.sort()
        result = []

        for i, a in enumerate(nums):
            #traverse the array
            #for every num i can run a two sum on rest of the array
            #since it is sorted i can do it with left and right pointer
            #also since it is sorted the numbers beyond any positive num will all be positive so this
            #wont give me a total sum of 0 ever and we can skip it
            if a>0:
                break #no need to evaluate beyond any positive number
            
            #also if it is not the first num, we should check if it is equal to last number and we can avoid the duplicate
            #number
            if i>0 and a == nums[i-1]:
                continue
            
            #otherwise run a two sum for compliment of this num on the rest of array
            target = -1*a

            left, right = i+1, len(nums)-1

            while left < right:
                if nums[left] + nums[right] > target:
                    right-=1
                elif nums[left] + nums[right] < target:
                    left+=1
                else:
                    #add to result
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    #to avoid repeated nums at both places we will skip till same from any one side
                    while left <right and nums[left] == nums[left-1]:
                        left+=1

            
        return result

        