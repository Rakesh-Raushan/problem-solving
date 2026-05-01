class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #at most two majority elements can exist here which have count > n/3 (else total will go beyond n)
        #so we will assume two candidates for the majority and track them and their counts
        candidate1, candidate2, count1, count2 = None, None, 0, 0

        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        #we have two candidates as potential majority, let's get their actual count to confirm
        act_count = {candidate1: 0, candidate2: 0}

        for n in nums:
            if n == candidate1:
                act_count[candidate1] += 1
            elif n == candidate2:
                act_count[candidate2] += 1
        thres = len(nums)/3
        return [candidate for candidate in act_count if act_count[candidate] > thres and candidate is not None]