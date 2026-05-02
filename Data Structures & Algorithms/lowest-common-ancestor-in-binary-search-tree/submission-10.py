# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def isInTree(root, r):
            if not root:
                return False
            if r.val == root.val:
                return True
            return isInTree(root.left, r) or isInTree(root.right, r)

        if not root:
            return root
        if root.val == p.val or root.val == q.val:
            return root

        p_in_left = isInTree(root.left, p)
        q_in_left = isInTree(root.left, q)

        if p_in_left != q_in_left:
            return root
        elif p_in_left:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        