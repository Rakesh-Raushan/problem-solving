class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #for a valid tree, it needs to be undirected which is already ensure
        #it needs to be acyclic i.e it needs to have n-1 edges for n nodes
        #it has to connected since even graph with n-1 edges may have disconnected components

        #check cycle
        if len(edges) !=n-1:
            return False

        #check if the graph has disconnected components
        #run a dfs from any one node and if the graph is connected, we will be able to visit all nodes

        #create adj list graph
        adj = {i:[] for i in range(n)}
        for src, dst in edges:
            #note undirected so create both direction edges
            adj[dst].append(src)
            adj[src].append(dst)

        #define a dfs func
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for adj_node in adj[node]:
                dfs(adj_node)
        
        #run dfs from any node
        dfs(0)
        #check if we visited all or not
        return len(visited)==n
        