# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #let's do a level order traversal BFS and gather nodes left to right in queue

        #explicit empty
        if not root:
            return []
        from collections import deque
        queue = deque([root])

        right_side_view = []
        while queue:
            #do level basis
            nodes_at_this_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                nodes_at_this_level.append(node)

                #process its children left to right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #collect the right most node at this level in right_side_view
            right_side_view.append(nodes_at_this_level[-1].val)
        
        return right_side_view


    #verify: [1], [], node=1, nl[1], q [2,3], rsv = [1]
    # [2,3] nl[2,3], rsv[1,3]
    #case []



        