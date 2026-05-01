"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #edge case: empty
        if not node:
            return
        #i can make use of a hashmap of old and new cloned nodes to clone the graph
        old_new_map = {}

        #then i can do an iterative dfs from start node

        def dfs(node):
            if not node in old_new_map:
                cloned_node = Node(val = node.val)
                old_new_map[node] = cloned_node
            
            for nei in node.neighbors:
                if nei not in old_new_map:
                    dfs(nei)
                cloned_node.neighbors.append(old_new_map[nei])
        
        dfs(node)
        
        return old_new_map[node]
        