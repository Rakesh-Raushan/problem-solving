# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.inorder_list = []
        def inorder_traversal(root):
            if not root:
                return
            
            #recurse on left
            inorder_traversal(root.left)
            self.inorder_list.append(root.val)
            # if i==k:
            #     return root.val
            # else:
            #     i+=1
            inorder_traversal(root.right)
        
        inorder_traversal(root)
        
        return  self.inorder_list[k-1]
        