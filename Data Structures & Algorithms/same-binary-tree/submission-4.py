# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        if not p:
            if not q:
                return True
            else:
                return False
        if not q:
            if not p:
                return True
            else:
                return False
        
        if p.val != q.val:
            return False
        
        #else act recursively on the children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)