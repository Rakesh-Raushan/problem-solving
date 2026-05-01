# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # if not root:
        #     new_node = TreeNode(val)
        #     return new_node
        # if val > root.val:
        #     root.right = self.insertIntoBST(root.right, val)
        # else:
        #     root.left = self.insertIntoBST(root.left, val)
        # return root
        if not root:
            return TreeNode(val)
        curr = root

        while True:
            if val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                else:
                    curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                else:
                    curr = curr.left


# 5 39 14, 6
# f(5), 6>5, 5.right = f(9,6), 6<9, 9.left = f(None, 6), 9.left = (6)
        

        