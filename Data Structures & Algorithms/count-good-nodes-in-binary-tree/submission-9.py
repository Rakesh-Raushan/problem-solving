# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 #no good nodes in empty tree
        
        def dfs(node, max_so_far):
            #check if null node
            if not node:
                return 0
            #if a good node, increase count
            count = 1 if node.val >= max_so_far else 0
            max_so_far = max(node.val, max_so_far) 

            count+=  dfs(node.left, max_so_far)
            count+=  dfs(node.right, max_so_far)

            return count
        
        return dfs(root, root.val)
