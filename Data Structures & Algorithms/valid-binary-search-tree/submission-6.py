# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #empty tree
        if not root:
            return True #empty is valid

        #we need to apply BST criterion but instead of node to node comparision which can happen only
        #for immediate nodes, we will compare each node to the range it is allowed to be in as we grow
        #the tree, since right subtree must have values greater than root, root becomes lower range (not included)
        # and since left subtree must have values lower than root, root becomes the upper range (not included)

        def check_range_dfs(root, low, high):
            if not root:
                return True
            #check root is in the permissible range
            if not (low < root.val < high):
                return False
            #recurse on its child with updated boundaries as per this root
            return check_range_dfs(root.left, low, root.val) and check_range_dfs(root.right, root.val, high)
        
        #call this function on root with infinite boundaries
        return check_range_dfs(root, float("-inf"), float("inf"))
            
        