# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #this is a code wise small problem but super tricky
        #the important gotcha is that although as the solution we want to return the max dia
        #which we can see from a small subtree [1,2,3] is sum of left and right depth
        #but the recursion to work, as the calculation at each node for max dia is dependent on the 
        #height of the subtree so the recursion requires us to return the height and not the max depth
        #so we do that and simply use a global variable of the class to update the max depth

        self.max_dia = 0 #this we will use to update the max_dia we traverse nodes

        #we use a recursive helper to help us achive the calculation of recursive nature but as part of solution
        # we do not return any value from the recursion but our self.max_dia which will update as recursion runs
        self.helper(root)
        return self.max_dia

    def helper(self, root):
        if not root:
            return 0 # since the height of a none subtree is zero
        #we calculate the depth for left and right
        left_depth = self.helper(root.left)
        right_depth = self.helper(root.right)

        #once we have this for a node, we know the max dia from that will be left_depth + right_depth
        #we compare it to our global max dia and update
        self.max_dia = max(self.max_dia, left_depth+right_depth)

        #now we need to return from the call so we ensure that for other calls we return back the right height for this tree
        #as per the depth of its left and right subtrees

        return 1 + max(left_depth, right_depth)
