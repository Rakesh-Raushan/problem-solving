# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #idea is simple, at every node, the max length is max of previous max or sum of the nodes left and right
        self.max_length = 0
        self.helper(root)
        return self.max_length

    def helper(self, root):
        if not root:
            return 0
        left_length = self.helper(root.left)
        right_length = self.helper(root.right)
        self.max_length = max(self.max_length, left_length + right_length)

        return max(left_length, right_length)+1
