# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s, e = 0, len(pairs)-1

        def quicksort_rec(pairs, s, e):
            if s>=e:
                return
            
            left, pivot = s, pairs[e]

            # partition operation
            # step1: iterate till pivot -1 pos
            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    #swap that ele with leftmost unswapped pos
                    pairs[i], pairs[left] = pairs[left], pairs[i]
                    # increase leftmost unswapped position pointer
                    left+=1
            
            # step2: at this left signifies the sorted position of pivot, so swap it
            pairs[e], pairs[left] = pairs[left], pairs[e]

            # now recurse this on left unsorted and right unsorted partitions
            quicksort_rec(pairs, s, left-1)
            quicksort_rec(pairs, left+1, e)
        
        quicksort_rec(pairs, s, e)

        return pairs



        