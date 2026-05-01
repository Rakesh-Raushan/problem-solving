# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        #idea of insertion sort:
        # a single ele is always sorted and inserting an ele in a sorted arr
        # is simply shifting that ele from right to left till it is sorted pos
        # i.e ele > ele left to it.
        # this idea can be applied on any arr by considering 1st ele as the single ele
        # which is sorted and then starting insertion from second ele to left arr
        # we take n-1 passes to insert all ele on right to grow this single ele sorted arr
        # to original sorted arr needed
        if not pairs:
            return []
        import copy
        states = [copy.copy(pairs)] # shalow copy like [pairs[:]] or [list(pairs)] will also work
        for i in range(1, len(pairs)):
            #for every pass we will try to insert ele at i into arr left to it
            # hence i-1 is the position we will start shifting it from
            j=i-1
            while(j>=0 and pairs[j].key > pairs[j+1].key):
                #swap them
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j-=1
            states.append(copy.copy(pairs))
        return states

        