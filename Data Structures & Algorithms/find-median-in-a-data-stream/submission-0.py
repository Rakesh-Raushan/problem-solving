class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        # push it to small one
        heapq.heappush(self.small, -1*(num))
        # check if max of small < min of large or not, if not then transfer to large
        if self.small and self.large and -1*(self.small[0]) > self.large[0]:
            larger_ele = -1* (heapq.heappop(self.small))
            heapq.heappush(self.large, larger_ele)

        # check for two halfs to be almost equal (diff of max 1)
        # check if small is large than by 1
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1* (heapq.heappop(self.small)))
        
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1* (heapq.heappop(self.large)))
        

    def findMedian(self) -> float:

        # if the small one is larger in len
        if len(self.small) > len(self.large):
            return -1 * (self.small[0])
        
        # if the large one is larger in len
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + self.large[0])/2
        
        