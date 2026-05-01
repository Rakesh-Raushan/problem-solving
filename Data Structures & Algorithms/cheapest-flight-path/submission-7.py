class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #no duplicate and no flights from an airport to itself
        #it means only one connection b/w any two adjacent nodes and no self loop for any node in graph
        #at most k stop means, src to dst evaluate all paths with max k in b/w node path length
        #and give the min cost one
        #i can apply djikstra's to find the shortest path to all nodes
        #no need for djikstra actually, i can do a dfs to get all paths with path length and cost
        #put them on a minheap based on cost, pop till you get max k stops else return -1
        adj = {i:[] for i in range(n)}
        for u, v, price in flights:
            adj[u].append((v,price))
        
        self.minprice = float("inf")

        def dfs(node, curr_cost, curr_path_len):
            if curr_path_len-2>k:
                return
            if node == dst:
                self.minprice = min(self.minprice, curr_cost)
                return
            for next_node, price in adj[node]:
                #no need to do if we are already at higher price
                if curr_cost+price >= self.minprice:
                    continue
                dfs(next_node, curr_cost+price, curr_path_len+1)
        
        dfs(src, 0, 1)
        
        return -1 if self.minprice == float("inf") else self.minprice

        #{0:[(1,200)], 1: [(2,100), (3,300)], 2:[(3,100)], 3:[]}
            


        