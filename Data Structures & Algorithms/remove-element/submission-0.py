class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for n in nums:
            if n==val:
                continue
            else:
                nums[idx] = n
                idx+=1
        return idx

    #dry run
    # nums = [1,1,2,3,4], val = 1
    # idx = 0, 1==1, skip
    # idx = 0, 1==1, skip
    # idx = 0, 2!=1, nums[0] = 2, nums = [2,1,2,3,4], idx = 1
    # idx = 1, 3!=1, nums[1] = 3, nums = [2,3,2,3,4], idx = 2
    # idx = 2, 4!=1, nums[2] = 4, nums = [2,3,4,3,4], idx = 3
    # return 3
        