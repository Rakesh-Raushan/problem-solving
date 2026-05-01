class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums = Counter(nums)
        for n in count_nums:
            if count_nums[n] > len(nums)/2:
                return n