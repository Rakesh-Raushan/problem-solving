class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        #adj list
        adj_list = {}
        for source, dest, wt in edges:
            if not source in adj_list:
                adj_list[source] = [[dest, wt]]
            else:
                adj_list[source].append([dest, wt])

        shortest_dist = {}

        #min heap, initialise with source
        minheap = [(0, src)]

        while minheap:
            node_weight, node = heapq.heappop(minheap)

            #if already visited, skip it
            if node in shortest_dist:
                continue
            
            shortest_dist[node] = node_weight

            #explore its neighbours
            neighbours = adj_list.get(node, [])

            for neighbour, neighbour_w in neighbours:
                if neighbour not in shortest_dist:
                    heapq.heappush(minheap, (node_weight + neighbour_w, neighbour))
            
        for i in range(n):
            if i not in shortest_dist:
                shortest_dist[i] = -1
            
        return shortest_dist



        

        