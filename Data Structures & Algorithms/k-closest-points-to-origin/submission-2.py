class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we can put the points on a heap and pop k times for closest k
        #but closest is in terms of distance so we can do it with a class

        class Point:
            def __init__(self,x,y):
                self.x = x
                self.y = y
                self.dist = x*x + y*y #squared dist is also okay for comparision
            
            #for comparision, define less than 
            def __lt__(self, other):
                return self.dist < other.dist

        #we can use this now to put point obj on heap

        minheap = [Point(x,y) for x,y in points]
        heapq.heapify(minheap)

        #get k closest
        result = []
        for _ in range(k):
            point_obj = heapq.heappop(minheap)
            #get x y
            result.append([point_obj.x, point_obj.y])
        return result

        