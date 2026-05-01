class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #without sorting, what if we use heap
        # i can create maxheap and pop it k time, heapify O(n), k pops = k(logn)
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        for _ in range(k):
            heap_num = heapq.heappop(max_heap)
        return -heap_num