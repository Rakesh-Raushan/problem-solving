class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort them so that we can skip over the duplicated when we want to exclude them from subset

        curr_set, results_set = [], []

        self.helper(0, nums, curr_set, results_set)

        return results_set

    def helper(self, i, nums, curr_set, results_set):
        #base case when we are at the depth of recursion and want to add a copy to result
        if i==len(nums):
            results_set.append(curr_set.copy())
            return
        
        # case when we are still on decision path w.r.t different nums inclusion exclusion
        # inclusion case
        curr_set.append(nums[i])
        #recurse for other nums
        self.helper(i+1, nums, curr_set, results_set)


        #exclusion case, remove the nums[i] added earlier
        curr_set.pop()
        # we also need to remove any other repetitions of the nums[i]
        while i+1 <len(nums) and nums[i] == nums[i+1]:
            i+=1 #skip them
        #after this just call recurse on the next num
        self.helper(i+1, nums, curr_set, results_set)
        