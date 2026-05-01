"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        

        old_new_map = {}
        def dfs(node):
            if node in old_new_map:
                return old_new_map[node]
            else:
                cloned_node = Node(val = node.val)
                old_new_map[node] = cloned_node
            
            for nei in node.neighbors:
                cloned_node.neighbors.append(dfs(nei))
            return cloned_node

        return dfs(node)
        

