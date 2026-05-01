# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #run a dfs to explore all paths and keep track of sum and path, if bigger sum, update sum and path
        #says path not necessarily need to include root, means any path possible, in such a case dfs needs to be run on all nodes in brute approach
        #so better approach will be to approach something like kadane's that only if the total sum in a path so far is positive take that else 0
        #in this scenario it mean to take path only node +left or node+right for returning in recursive call
        self.max_sum=float("-inf")

        def dfs(root):
            if not root:
                return 0

            left_sum = max(0, dfs(root.left))
            right_sum = max(0, dfs(root.right))

            #check if path via this node is the best
            self.max_sum = max(self.max_sum, left_sum+ root.val+right_sum)

            #return the best path via(left or right) with this node for calculations in its parent node
            return root.val + max(left_sum,right_sum)

        dfs(root)

        return self.max_sum
        