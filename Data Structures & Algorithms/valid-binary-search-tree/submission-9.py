# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #idea is root can have any value but for children of any root
        #left child must lie in a range bounded to right by its root
        #right child must lie in a range bounded to left by its root

        if not root:
            return True #empty tree

        def is_in_range(node, min_val, max_val):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            else:
                return is_in_range(node.left, min_val, node.val) and is_in_range(node.right,node.val,max_val)
        
        return is_in_range(root, float("-inf"), float("inf"))
        