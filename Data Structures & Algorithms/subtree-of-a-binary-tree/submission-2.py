# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #i think we can just use the idea of is same tree to do this
        #i canr ecurse to find the root in other, if i find, i do is sametree else false
        if not subRoot:
            return True
        if not root:
            return False
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif (p and q and p.val != q.val) or (q and not p) or (p and not q):
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        