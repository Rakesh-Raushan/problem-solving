class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #no duplicate and no flights from an airport to itself
        #it means only one connection b/w any two adjacent nodes and no self loop for any node in graph
        #at most k stop means, src to dst evaluate all paths with max k in b/w node path length
        #and give the min cost one
        #i can apply djikstra's to find the shortest path to all nodes
        #no need for djikstra actually, i can do a dfs to get all paths with path length and cost
        #put them on a minheap based on cost, pop till you get max k stops else return -1
        # adj = {i:[] for i in range(n)}
        # for u, v, price in flights:
        #     adj[u].append((v,price))
        
        # self.minprice = float("inf")

        # def dfs(node, curr_cost, curr_path_len):
        #     if curr_path_len-2>k:
        #         return
        #     if node == dst:
        #         self.minprice = min(self.minprice, curr_cost)
        #         return
        #     for next_node, price in adj[node]:
        #         #no need to do if we are already at higher price
        #         if curr_cost+price >= self.minprice:
        #             continue
        #         dfs(next_node, curr_cost+price, curr_path_len+1)
        
        # dfs(src, 0, 1)
        
        # return -1 if self.minprice == float("inf") else self.minprice

        #this is not optimal as time complexity in worst case will be O((n-1)^(k+1)) exponential
        # we may end up trying for each n-1 stops(except dest) till the k+1 stops limit breach (as we dont 
        # have cycles prevention through visited )

        #better approach is bellman ford like approach
        #assume prices to each node is initially infinity

        prices = [float("inf")]*n
        #price from source = 0
        prices[src]=0
        #we can iterate on edges to update min prices repeatedly based untill we have more than k stops
        for _ in range(k+1):
            #k+1 since we need k stops excluding src and dest
            temp_prices = prices[:] #a copy of prices 
            for s, d, p in flights:
                #if this price is smaller than curr global price, update this to temp_prices
                #but since we may have the inf price, we must continue if that is the case
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            prices = temp_prices[:]
        #after k+1 iterations our temp_prices is the one we wanted to have
        return -1 if temp_prices[dst] == float("inf") else temp_prices[dst]


        #{0:[(1,200)], 1: [(2,100), (3,300)], 2:[(3,100)], 3:[]}
            


        