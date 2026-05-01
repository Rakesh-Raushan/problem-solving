# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #empty tree, nothing to invert so we just return root or none
        if not root:
            return root
        
        #for a root then we swap its children
        root.left, root.right = root.right, root.left
        #then we recursively repeat this for its left and right child
        self.invertTree(root.left)
        self.invertTree(root.right)
        #then we return the root with the children swapped back to the caller
        return root

        
        