# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, left_pairs, right_pairs):
        merged_pairs = [0]*(len(left_pairs) + len(right_pairs))
        i, j, k = 0, 0, 0
        while(i < len(left_pairs) and j < len(right_pairs)):
            if left_pairs[i].key < right_pairs[j].key:
                merged_pairs[k] = left_pairs[i]
                i+=1
                k+=1
            elif left_pairs[i].key > right_pairs[j].key:
                merged_pairs[k] = right_pairs[j]
                j+=1
                k+=1
            else:
                merged_pairs[k] = left_pairs[i]
                i+=1
                k+=1
                merged_pairs[k] = right_pairs[j]
                j+=1
                k+=1
        #copy rest
        while(i < len(left_pairs)):
            merged_pairs[k] = left_pairs[i]
            i+=1
            k+=1
        while(j < len(right_pairs)):
            merged_pairs[k] = right_pairs[j]
            j+=1
            k+=1
        return merged_pairs


    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        #idea: divide it into two recursively till it becomes 1 size
        # base case of 1 is always sorted so just return it
        # on returned items, apply merging of 2 sorted arr operation

        #empty list
        if not pairs:
            return []
        #base case, one ele arr always sorted
        if len(pairs)==1:
            return pairs
        #find mid
        mid = len(pairs)//2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])

        return self.merge(left,right)