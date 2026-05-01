class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        #adj list
        adj_list = {}
        for source, dest, wt in edges:
            if not source in adj_list:
                adj_list[source] = [[dest, wt]]
            else:
                adj_list[source].append([dest, wt])
        
        #visited track
        visited = set()

        #initial state, src to src =0 rest all inf
        shortest_dist = {x:float("inf") for x in range(n)}
        shortest_dist[src] = 0

        #min heap, initialise with source
        minheap = [(0, src)]

        while minheap:
            w, n = heapq.heappop(minheap)

            #if already visited
            if n in visited:
                continue
            
            #mark visited
            visited.add(n)

            #explore its neighbours
            neighbours = adj_list.get(n, [])

            for neighbour, nw in neighbours:
                # new_dist = currnode w + neighbourdist
                new_dist = w + nw
                shortest_dist[neighbour] = min(shortest_dist[neighbour], new_dist)
                #explore other path while backtrack only if an improvement in the distance
                heapq.heappush(minheap, (new_dist, neighbour))
            
        #update dist of unreachable nodes
        for node in shortest_dist:
            if shortest_dist[node] == float("inf"):
                shortest_dist[node] = -1
            
        return shortest_dist



        

        