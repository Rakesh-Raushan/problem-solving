# class Solution:
#     def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
#         #adjlist and wt dict
#         adj_list = {}
#         wt_map = {}

#         for s, dest, wt in edges:
#             if s in adj_list:
#                 adj_list[s].append(dest)
#             else:
#                 adj_list[s] = [dest]
#             wt_map[(s,dest)] = wt
        
#         heap = []
#         shortest_dist = {x:-1 for x in range(n)}
        
#         heapq.heappush(heap, (0,src))

#         while heap:
#             wt, node = heapq.heappop(heap)
#             if shortest_dist[node] < 0 or shortest_dist[node] >wt:
#                 shortest_dist[node] = wt
#             else:
#                 continue

#             neighbours = adj_list.get(node, [])
#             for neighbour in neighbours:
#                 heapq.heappush(heap, (wt + wt_map[(node, neighbour)], neighbour))
        
#         return shortest_dist

#         #dry run
#         #(0,0), sd{n0:0}
#         #[(3,n2),(10,n1)], 3,n2, sd{n0:0, n2:3}, n2->n1,n4,n3
#         #[(10,n1), (7,n1), (5,n4), (11,n3)]
#         #[(10,n1), (7,n1), (11,n3)] wt5,n4, sd{n0:0, n2:3, n4:5}neigh no neighbours
#         #[(10,n1), (11,n3)] wt7,n1, sd{n0:0, n2:3, n4:5, n1:7}, neigh n1 (n3(7+2))
#         #[(10,n1), (11,n3), (9, n3)],
#         #[(10,n1), (11,n3)], n3,wt9, sd{n0:0, n2:3, n4:5, n1:7, n3:9} neigh n4(9,5)
            

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Create adjacency list
        adj_list = {}
        for s, dest, wt in edges:
            if s not in adj_list:
                adj_list[s] = []
            adj_list[s].append((dest, wt))  # Store weight directly in adjacency list
        
        # Initialize distances
        shortest_dist = {i: float('inf') for i in range(n)}
        shortest_dist[src] = 0
        
        # Priority queue
        heap = [(0, src)]
        visited = set()
        
        while heap:
            dist, node = heapq.heappop(heap)
            
            # Skip if we've already processed this node
            if node in visited:
                continue
            
            visited.add(node)
            
            # Process neighbors
            for neighbor, weight in adj_list.get(node, []):
                # Only process if we can improve the path
                new_dist = dist + weight
                if new_dist < shortest_dist[neighbor]:
                    shortest_dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
        
        # Convert infinity values to -1 if needed
        for node in shortest_dist:
            if shortest_dist[node] == float('inf'):
                shortest_dist[node] = -1
                
        return shortest_dist