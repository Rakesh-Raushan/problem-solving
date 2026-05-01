# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #null tree or tree with one node
        if not root or (not root.left and not root.right):
            return root
        #swap left and right children
        root.left, root.right = root.right, root.left

        #recurse this on left and right child
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root
        