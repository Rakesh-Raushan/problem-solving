class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        #form adj
        from collections import defaultdict
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
        
        shortest_path = {}
        min_heap = [(0, src)] #src weight assumed zero as it is starting point

        while min_heap:
            wt, node = heapq.heappop(min_heap)

            if node in shortest_path:
                continue
            shortest_path[node] = wt

            for adj_node, adj_node_wt in adj[node]:
                if not adj_node in shortest_path:
                    heapq.heappush(min_heap, (wt+adj_node_wt, adj_node))
        
        for i in range(n):
            if i not in shortest_path:
                shortest_path[i] = -1
        
        return shortest_path



