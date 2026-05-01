# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #since it is a BST, the lowest common ancestor would be the node which branches out the
        #2 given vals or say the node which is greater than one but less than other
        #atleast 2 nodes will be there as from constraints
        # if p.val < root.val < q.val or q.val < root.val < p.val:
        #     return root
        # #compare with children recursively
        # self.lowestCommonAncestor(root.left, p, q)
        # self.lowestCommonAncestor(root.right, p, q)
        self.lca = None
        def dfs(node):
            if not node:
                return
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                self.lca = node
                return
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.lca




        