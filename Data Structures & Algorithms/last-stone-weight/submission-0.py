class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #since we need to repeatedly pick two largest, max heap is best suited
        self.maxheap = [-1*w for w in stones]
        #convert to max heap
        heapq.heapify(self.maxheap)

        while len(self.maxheap) > 1:
            #pick two
            s1 = heapq.heappop(self.maxheap)*-1
            s2 = heapq.heappop(self.maxheap)*-1

            if s1>s2:
                heapq.heappush(self.maxheap, s2-s1)
            elif s2>s1:
                heapq.heappush(self.maxheap, s1-s2)
            #do nothing if rqual as both destroyed
        
        return self.maxheap[0]*-1 if self.maxheap else 0
        