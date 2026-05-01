class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        #let's take the dfs approach
        # we would iterate on each node to run a dfs, but before that let's build an adj list

        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for u,v in edges:
            adj_list[u].append(v)

        #to collect the results, we will initialize a list and also a visited set to capture visited

        visited = set()
        path = set() #to handle the case of cycle presence
        topsorted = []

        #iterate and dfs on each node
        for i in range(n):
            if i not in visited:
                if not self.dfs(i, adj_list, visited, path, topsorted):
                    return []
        
        return topsorted[::-1]

    #let's define the dfs that we will apply on each node
    #idea of dfs is to recurse as long as there is an edge of child to cover the child node first before any parent
    #and only when we backtrack we will add the node or the parent to the topsorted list

    def dfs(self, node, adj_list, visited, path, topsorted):
        #base case, return if a node is already visited
        if node in path:
            return False
        if node in visited:
            return True

        path.add(node)
        #recurse dfs on all its neighbours 
        for neighour in adj_list[node]:
            if not self.dfs(neighour, adj_list, visited, path, topsorted):
                return False
        
        #node has covered all children possible on this path, so add it to topsort
        topsorted.append(node)

        #we mark it visited
        visited.add(node)
        #remove from path for full exploration
        path.remove(node)
        
        return True


#TODO: add cycle detection logic
        