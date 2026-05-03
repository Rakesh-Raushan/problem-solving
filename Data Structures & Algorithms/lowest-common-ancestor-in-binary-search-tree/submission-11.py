# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #important fact to notice here is that it is BST
        #now bst means for every node: node.left < node < node.right
        #additionally for Lowest common ancestor, it has to be the node whose 
        if p.val > q.val:
            p,q = q, p #ensure p is smaller one
        
        def dfs(root, p, q):
            if p.val <= root.val and q.val >= root.val:
                return root
            elif q.val < root.val:
                #greater of two is smaller than root -> both are smaller than root
                return dfs(root.left, p, q)
            elif p.val > root.val:
                #smaller of two is greater than root -> both are greater than root
                return dfs(root.right, p, q)
        
        return dfs(root, p, q)
        
        
        