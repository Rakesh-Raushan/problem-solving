# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque

        queue = deque([root])
        result = []

        while queue:
            nodes_at_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                nodes_at_level.append(node.val)
                #check children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #add all nodes from the level to result
            result.append(nodes_at_level)
        return result

        