class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0,nums)

    def helper(self, i, nums):
        #base case: we have i out of bounds
        if i==len(nums):
            return [[]] #a blank list of list to initiate the collection of perms

        #for this i, initialise a resulting perms list
        res_perms = []

        # recurse ahead to next i and collect all perms from it
        perms = self.helper(i+1, nums)

        # act on each perm returned and insert nums[i] at each possible pos
        for p in perms:
            for j in range(len(p)+1):
                #len +1 since we consider beginning and end as pos as well
                #create a copy of perm before inserting
                p_copy = p[:]
                # insert at j, nums[i]
                p_copy.insert(j, nums[i])
                # this needs to be collected in perms for this level
                res_perms.append(p_copy)

        return res_perms

         