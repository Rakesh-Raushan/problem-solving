class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     count_nums = Counter(nums)
    #     for n in count_nums:
    #         if count_nums[n] > len(nums)/2:
    #             return n
        #above sol is O(n) in both time and space, can we do in linear time but constant space
    def majorityElement(self, nums: List[int]) -> int:
        #there is an algo called boyer-moore voting algo that solves it
        #the idea is simple that in a voting process, the majority always outlasts the others, i.e 
        #the majority person will always have at least one or more votes left if we start cancelling votes for every different candidate
        #the algo involves, a candidate and a count variable
        #pseudo code:
        #idea:
        #[5,5,1,1,1,5,5], intially count=0, candidate = None
        # 5 -> count==0, so candidate =5, count=1
        # 5 -> count!=0 and ==candidate, so count=2
        # 1 -> count!=0 and !=candidate so count=1
        # 1 -> count!=0 and !=candidate so count=0
        # 1 -> count==0, so candidate =1, count=1
        # 5 -> count!=0 and !=candidate, count=0
        # 5 -> count=0 so candidate=5, count=1
        #return 5
        #if count is zero, candidate = curr_ele and count=1 (essentially forget everything before it, who ever is majorty in rest is the majority)
        #elif existing candidate == curr_ele, increase count by 1
        #else decrease count by 1
        #after traversing the entire list, return candidate

        candidate, count = None, 0
        for n in nums:
            if count == 0:
                #all prev ele in list do not matter, start fresh lookout for majority ele here onwards
                candidate, count = n, 1
            elif n == candidate:
                #same ele so increase its count by 1
                count += 1
            else:
                #diff ele so cancel count of current candidate by 1
                count -= 1
        #majority will outlast all others combined in voting with cancellation, so current candidate should be the majority
        return candidate
        