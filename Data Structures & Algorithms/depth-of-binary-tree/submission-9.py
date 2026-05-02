# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
max_depth = 0

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
# 1 (1,0) -> md = 0, cd = 0, cd = 1, md = 1,
#       left of 1: 2 (2,1) -> cd = 2, md =  2, 
#           left of 2: null (null, 2) -> return
#           right of 2: null (null, 2) -> return
#       right of 1: 3 (3,1) -> cd = 2, md = 2
#           left of 3: (4,2) -> cd = 3, md = 3
#               left of 4 -> null -> return
#               right of 4 -> null -> return
#           right of 3 -> null -> return
# main func return max_depth = 3