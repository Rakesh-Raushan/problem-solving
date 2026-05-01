# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #first apply the usual template of both none, one none and both not none
        if not root and not subRoot:
            #both are None
            return True
        elif not root or not subRoot:
            #one is None
            return False
        else:
            #both not None
            #check if root and subRoot are same tree
            if self.isSameTree(root, subRoot):
                #same tree so is a subroot
                return True
            else:
                #not same tree, so recurse on children to check if any one can be subRoot
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            #both are None
            return True
        elif not p or not q:
            #one is None
            return False
        else:
            if p.val != q.val:
                return False
            #both not none so compare children
            return self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right)


        