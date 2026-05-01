# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #let;s do simply this first, get height func in place, use that to check balanced recursively
        if not root:
            return True
        left_h = self.getHeight(root.left)
        rt_h = self.getHeight(root.right)
        if abs(left_h - rt_h) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        