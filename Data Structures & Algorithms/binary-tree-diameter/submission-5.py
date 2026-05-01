# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_dia = 0

        def dfs(node):
            if not node:
                return 0
            
            #get left and right
            left = dfs(node.left)
            right = dfs(node.right)

            #check if path via this node is max dia and update if so
            self.max_dia = max(self.max_dia, left + right)

            #if not return to its root with max left or right possible
            return 1 + max(left, right)
        dfs(root)

        return self.max_dia
        