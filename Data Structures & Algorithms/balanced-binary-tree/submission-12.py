# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getHeight(root):
    if not root:
        return 0
    else:
        return 1 + max(getHeight(root.left), getHeight(root.right))

# 123nullnull4null5
# 1+ max(0, getH(3)) = 1 + max(0, 1 + max(0, getH(4))) = 1 + max(0, 1 + max(0, 1+ max(0, getH(5))))
# = 1 + 2 = 3

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #since by definition left and right tree heights must not differ by more than 1
        #for every subtree, we can think of doing it by recursion
        #so, when abs(h_left - h_right) > 1 return Fail
        if not root:
            return True
        elif abs(getHeight(root.left) - getHeight(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
        