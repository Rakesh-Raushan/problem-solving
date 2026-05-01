# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(node):
            if not node:
                return 0
            
            left_h = dfs(node.left)
            right_h = dfs(node.right)

            if abs(left_h - right_h) > 1:
                self.balanced = False
                return -1
            height_this_root = 1 + max(left_h, right_h)

            return height_this_root


        dfs(root)
        return self.balanced

        
            

        