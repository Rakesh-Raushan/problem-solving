class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {i:[] for i in range(1, n+1)}
        for src, dst, time in times:
            adj[src].append((dst, time))
        
        minheap = [(0,k)]
        visited = set()
        t = 0
        while minheap:
            time, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            t = time
            for nei_node, nei_node_t in adj[node]:
                if nei_node not in visited:
                    heapq.heappush(minheap, (t+nei_node_t, nei_node))
        
        return t if len(visited)==n else -1
            





        