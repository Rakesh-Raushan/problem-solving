class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result_set = set()
        for i in range(len(sorted_nums)):
            target = -1*sorted_nums[i]

            arr = sorted_nums[:i] + sorted_nums[i+1:]

            j, k = 0, len(sorted_nums)-2

            while(j<k):
                if arr[j] + arr[k] == target:
                    triplet = tuple(sorted([-1*target, arr[j], arr[k]]))
                    result_set.add(triplet)
                    j+=1
                    k-=1
                elif arr[j] + arr[k] > target:
                    k-=1
                else:
                    j+=1
        
        return [list(x) for x in result_set]



        