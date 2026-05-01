# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def get_list(root):
            if not root:
                return
            get_list(root.left)
            result.append(root.val)
            get_list(root.right)
        get_list(root)

        return result