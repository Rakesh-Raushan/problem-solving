# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.helper(root)
        return self.balanced

    def helper(self, root):
        if not root:
            return 0 #height of a empty tree
        left_height = self.helper(root.left)
        right_height = self.helper(root.right)

        #check the balanced criteria and continue only if it is balanced else update the global and return
        if not abs(left_height - right_height) <=1:
            self.balanced = False
            return -1
        # if not self.balanced:
        #     return #stop further recursion if not balanced found at a root

        #calculate the height at this root to return for comparision at higher level
        height_this_root = 1+ max(left_height, right_height)

        return height_this_root

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         self.balanced = True  # Set balanced flag initially
#         self.helper(root)
#         return self.balanced

#     def helper(self, root):
#         if not root:
#             return 0  # Height of an empty tree is 0
        
#         # Recurse for left and right subtrees
#         left_height = self.helper(root.left)
#         right_height = self.helper(root.right)

#         # Check if the current node is unbalanced
#         if abs(left_height - right_height) > 1:
#             self.balanced = False  # Tree is unbalanced
#             return -1  # Return a sentinel value to indicate an unbalanced state
        
#         # If balanced, return the height of the current node
#         return 1 + max(left_height, right_height)

        