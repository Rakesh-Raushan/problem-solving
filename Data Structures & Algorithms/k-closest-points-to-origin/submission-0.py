class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # class comparable_coord:
        #     def __init__(self,x,y):
        #         self.x = x
        #         self.y = y
            
        #     def __lt__(x,y):
        #         return x < y

        #create a distances list and make it a minheap
        dist_sq = [(-(p[0]*p[0] + p[1]*p[1]), i, p) for i, p in enumerate(points)]
        heapq.heapify(dist_sq)

        while len(dist_sq) > k:
            heapq.heappop(dist_sq)
        
        return [d[2] for d in dist_sq] if points and points[0] else []

    #verify points = [[0,2],[2,2]], k = 1
    #dist_sq = [-4, -8]; dist_sq_x_y_map [-4: [0,2], -8: [2,2]], dist_sq = [-4, -8], [-4]; [0,2]


        