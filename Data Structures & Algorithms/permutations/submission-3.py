class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return self.helper(0,nums)
        return self.helper2(nums)

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
    
    # the iterative approach
    def helper2(self,nums):
        # start with a blank list of list
        perms = [[]]

        #iterate through each n in nums
        for n in nums:
            #create a frest list for collecting the next set of nums with this n included
            perms_with_n = []
            for p in perms:
                #insert at each pos possible for p after making a copy of it
                for j in range(len(p)+1):
                    p_copy = p[:]
                    p_copy.insert(j, n)
                    #add it to perms_with_n
                    perms_with_n.append(p_copy)
            #update perms for next num to this one
            perms = perms_with_n
        
        #finally return the perms
        return perms


         