# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0

        self.helper(root)
        return self.max_dia

    def helper(self, root):
        #BASE, no node case, its height will be zero
        if not root:
            return 0
        
        #else check the left and right
        left_h = self.helper(root.left)
        right_h = self.helper(root.right)

        #update the dia based on these
        self.max_dia = max(self.max_dia, left_h+right_h)

        #for the last root, return incremented height
        return 1 + max(left_h, right_h)


            
        