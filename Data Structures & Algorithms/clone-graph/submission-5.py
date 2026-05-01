"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #8.07#
        #no node case
        if not node:
            return None
        #single node
        if not node.neighbors:
            new_node = Node(node.val)
            return new_node
        #more than one node
        start = node
        stack = [node]

        old_new_map = {}

        while stack:
            node = stack.pop()
            if node not in old_new_map:
                new_node = Node(val = node.val)
                old_new_map[node] = new_node
            else:
                new_node = old_new_map[node]
            for neighbor in node.neighbors:
                if neighbor in old_new_map:
                    new_node.neighbors.append(old_new_map[neighbor])
                else:
                    new_neighbor = Node(val = neighbor.val)
                    old_new_map[neighbor] = new_neighbor
                    new_node.neighbors.append(new_neighbor)
                    stack.append(neighbor)
        
        return old_new_map[start]

        #verify; [[2],[1,3],[2]]
        #stack = [(1)], node = (1, [2]), new_node = (1, []), old_new_map = {old1 : new1}, old1 neigh = [2], neigh = (2), new_neigh=(2)
        #{old1 : new1, old2 : new2}, new_node = (1, [2]) stack= [(2)];
        #node = (2, [1,3]), new_node = new2, neighbor = 1, (2, [1, 3]), (3), new_neighbour = 
        