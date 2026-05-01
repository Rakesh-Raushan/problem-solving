class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # val_id_map = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in val_id_map:
        #         result = [val_id_map[diff], i]
        #         return result
        #     else:
        #         val_id_map[nums[i]] = i

        seen = dict()

        for i,num in enumerate(nums):
            num_compliment = target - num
            if num_compliment in seen:
                return [seen[num_compliment],i]
            else:
                seen[num] = i
        
        #verify [3,4,5,6], seen = {}
        #0,3 -> compliment = 4, not in seen, so add this num {3:0}
        #1,4 -> compliment = 3, in seen so return [0,1]
        

        