class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #so we can take the greedy approach of djikstra's algo to find the min time
        #also we can check at the end if we got the min time for all the node else return -1

        #k is source node
        #if we put all the nodes on a minheap
        # [1,]
        min_time = [float("inf")] * (n+1) #1 indexed so 0 index irrelevant
        min_time[k] = 0

        #create adj list
        adj = {i: [] for i in range(1,n+1)}
        for u,v,t in times:
            adj[u].append((v,t))
        

        def dfs(node, time_to_node):
            if time_to_node > min_time[node]:
                return
            min_time[node] = time_to_node

            for nei, t in adj[node]:
                dfs(nei, time_to_node+t)
        
        dfs(k, 0)
        print(min_time)

        for i in range(1, n+1):
            if min_time[i] == float("inf"):
                return -1
        return max(min_time[1:])

        