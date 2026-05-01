"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         #empty head
#         if not head:
#             return None
        
#         #traverse list to first form fresh nodes with correct next and keep them mapped in a map of old to new nodes

#         node_map = {}
#         new_head = Node(x=head.val)

#         curr1, curr2 = new_head, head
        
#         while(curr2):
#             if curr2.next:
#                 next_val = curr2.next.val
#             else:
#                 next_val = None
#             node_map[curr2] = curr1
#             if next_val:
#                 curr1.next = Node(x=next_val)
#                 curr1 = curr1.next
#             else:
#                 curr1.next = next_val #none case
#             curr2 = curr2.next

#         #we have another LL deep copied except for the random
#         #use the old to new mapping to update random in each new
#         for old_node in node_map:
#             new_node = node_map[old_node]
#             if old_node.random:
#                 new_node.random = node_map[old_node.random]
#             else:
#                 #where random points to None
#                 new_node.random = None

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node_map = {}
        new_head = Node(x=head.val)

        curr_old, curr_new = head, new_head
        
        while curr_old:
            node_map[curr_old] = curr_new
            if curr_old.next:
                curr_new.next = Node(x=curr_old.next.val)
            curr_old = curr_old.next
            curr_new = curr_new.next if curr_new.next else None

        # Set up the random pointers
        for old_node, new_node in node_map.items():
            if old_node.random:
                new_node.random = node_map[old_node.random]
            else:
                new_node.random = None
        
        return new_head
        
