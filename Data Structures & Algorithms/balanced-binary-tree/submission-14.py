# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     #let;s do simply this first, get height func in place, use that to check balanced recursively
    #     if not root:
    #         return True
    #     left_h = self.getHeight(root.left)
    #     rt_h = self.getHeight(root.right)
    #     if abs(left_h - rt_h) > 1:
    #         return False
    #     else:
    #         return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    # def getHeight(self, root):
    #     if not root:
    #         return 0
    #     else:
    #         return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    # now this solution works but if we look at it, we are going to a node and to check if it is 
    # balanced, we are doing its height calculation going to all its nodes and we are doing this for
    # all nodes, for a balanced tree its like n + n/2 + n/4 + ... = O(nlogn) and for a skewed it can be
    # n + n-1 + n-2 + ... + 1 = n(n+1)/2 = O(n^2)
    # but if do the isbalanced and height cal together we can get O(N) as we will just visit everynode once
    # we can do so by writing a dfs that return both the balanced and height info in one go

        return self.dfs(root)[0]

    def dfs(self, root):
        if not root:
            return [True, 0] #isbalanced and height info both
        left, right = self.dfs(root.left), self.dfs(root.right)
        if not left[0] or not right[0]:
            return [False, 1 + max(left[1], right[1])] #either is not balanced
        elif abs(left[1] - right[1]) > 1:
            return [False, 1 + max(left[1], right[1])] # left and right are balanced but curr node is not balanced
        else:
            #propagate the height and balanced info
            return [True, 1 + max(left[1], right[1])]

        