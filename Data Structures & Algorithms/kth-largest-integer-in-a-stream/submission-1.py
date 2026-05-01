class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #create a minheap
        self.minheap = nums
        #heapify this list
        heapq.heapify(self.minheap)
        self.k = k
        #remove everythin other than smallest k
        while len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
        

    def add(self, val: int) -> int:
        #add this our minheap
        heapq.heappush(self.minheap, val)
        #check if the size got disturbed as we plan to maintain only k smalles so that o(1) access to kth largest is there on other end of heap
        if len(self.minheap) > self.k:
            #remove ele
            heapq.heappop(self.minheap)
        #since minheap of k size, 1st ele is kth largest
        return self.minheap[0]
        
