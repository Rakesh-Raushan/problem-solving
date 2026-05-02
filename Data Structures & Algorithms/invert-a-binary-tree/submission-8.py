# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root:
                return root
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        dfs(root)
        return root


# 1[1,2,3,4,5,6,7] -> [1,3,2,6,7,4,5]]
    #3 [1,3,2,7,6.4,5]
        #7 []
        