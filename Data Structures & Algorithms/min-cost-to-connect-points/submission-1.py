class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #in order to get the minimum cost to connect all points we can think of it as a spanning tree prob
        #and see if we have a valid MST, if so we return that
        #we can use either prims algo or kruskals algo
        #using prims algo
        n_edges = len(points)
        visited = set()
        minheap = [(0,0)] # (cost, point_index)
        total_cost = 0

        while len(visited) < n_edges:
            cost, i = heapq.heappop(minheap)
            if i in visited:
                continue
            
            visited.add(i)
            total_cost+=cost

            for j in range(n_edges):
                if j not in visited:
                    manh_dist = abs(points[i][0] - points[j][0]) +  abs(points[i][1] - points[j][1])
                    heapq.heappush(minheap, (manh_dist,j))
        
        return total_cost



            



            
            
        