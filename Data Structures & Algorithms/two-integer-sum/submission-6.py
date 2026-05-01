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

        seen_map = dict()
        for i, num in enumerate(nums):
            if target-num in seen_map:
                return [seen_map[target-num], i]
            else:
                seen_map[num] = i
        

        