class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        count_map = Counter(nums)

        maxheap = []

        for num, num_count in count_map.items():
            val = (-1*num_count, num)
            heapq.heappush(maxheap, val)
        
        result = []

        for i in range(k):
            result.append(heapq.heappop(maxheap)[1])
        
        return result

        