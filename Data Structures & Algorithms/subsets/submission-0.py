class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_set, results_set = [], []
        self.helper(0, nums, curr_set, results_set)
        return results_set

    def helper(self,i, nums, curr_set, results_set):

        #the base case when we have reached full depth on decision tree
        if i==len(nums):
            results_set.append(curr_set.copy())
            return
        
        #else, consider the two cases of including i vs excluding i
        #include i
        curr_set.append(nums[i])
        #recurse on the other paths which include this nums[i]
        self.helper(i+1, nums, curr_set, results_set)

        #exclude i and recurse
        curr_set.pop()
        self.helper(i+1, nums, curr_set, results_set)
        