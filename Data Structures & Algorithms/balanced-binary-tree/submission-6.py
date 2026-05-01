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
            #stop further recursion if not balanced found at a root
            self.balanced = False
            return -1 #if you do blank return it may fail somewhere as  it would actually try operations on return of this None and some int


        #calculate the height at this root to return for comparision at higher level
        height_this_root = 1+ max(left_height, right_height)

        return height_this_root

        