class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_rt = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = max_rt
            max_rt = max(temp, max_rt)
        return arr




# arr = [2,4,5,3,1,2]
# brute: at 0, [4,5,3,1,2] get max replace it
# at 1, [5,3,1,2] get max replace it
# till you are at last ele when you replace it with -1
# but this is n time finding max so O(n^2)
# if i start from the end
# i can say max_rt=2, replace it with -1
# move left, hold it in temp, replace it with its rt_max [2,4,5,3,2,-1] and update max
# max_rt = max(1, 2) so max_rt remains 2
# move left hold it in temp,replace it with its rt_max [2,4,5,2,2,-1], max_rt=3
# move left, temp = 5, [2,4,3,2,2,-1], max_rt =5
# move left, temp = 4, [2,5,3,2,2,-1], max_rt = 5
# move left, temp = 2, [5,5,3,2,2,-1], max_rt = 5
# no more left, this way in O(n)
        