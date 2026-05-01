# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #brute force way would be to just go to everynode 
        #calculate the height of that node left and right sub and check isbalanced
        #this would lead to n(logn) for balanced tree and for a skewed tree can go even n^2
        #brute implementation
        def getHeight(root):
            #no node has 0 height
            if not root:
                return 0
            #otherwise height is max of height of its two subtrees + 1 extra node to its subtree
            return 1+ max(getHeight(root.left), getHeight(root.right))
        
        if not root:
            return True
        #no node tree is balanced so true
        #else check this tree is balanced and also both its subtree are balanced
        elif abs(getHeight(root.left) - getHeight(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        