class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        #adjlist
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for u, v, w in edges:
            adj[u].append([v,w])
            #both ways
            adj[v].append([u,w])


        minheap = []
        visited = set()
        mst = []

        #initialise the minheap
        #selct a random node, say 0

        for neighbor, neighbor_wt in adj[0]:
            heapq.heappush(minheap, (neighbor_wt, 0, neighbor))
        
        #mark 0 visited
        visited.add(0)

        while minheap:
            node_wt, src, node = heapq.heappop(minheap)

            if node in visited:
                continue
            
            visited.add(node)

            #add it to our mst
            mst.append([node_wt, src,node])

            for neighbor, neighbor_wt in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(minheap, (neighbor_wt, node, neighbor))
        print(mst)
        return sum([x[0] for x in mst]) if len(visited)==n else -1
        #adj
        #{  
        #   0: [[1,10], [2,3]], 
        #   1: [[0,10], [3,2], [2,4]],
        #   2: [[0,3], [1,4],[3,8], [4,2]],
        #   3: [[1,2],[2,8], [4,5]], 
        #   4:[[2,2], [3,5]]
        #}minheap - [[10,0,1],[3,0,2]] -> [[10,0,1], [4,2,1], [8,2,3],[2,3,1]]
        #visited - (0) -> (0,2,4,3) 
        #mst = [[3,0,2]] -> [[3,0,2], [2,2,4],[5,4,3],[2,3,1]]

