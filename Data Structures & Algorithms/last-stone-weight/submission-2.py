class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #since we need to repeatedly pick two largest, max heap is best suited
        maxheap = [-1*w for w in stones]
        #convert to max heap
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            #pick two
            s1 = heapq.heappop(maxheap)*-1
            s2 = heapq.heappop(maxheap)*-1

            if s1>s2:
                heapq.heappush(maxheap, s2-s1)
            elif s2>s1:
                heapq.heappush(maxheap, s1-s2)
            #do nothing if rqual as both destroyed
        
        return maxheap[0]*-1 if maxheap else 0
        