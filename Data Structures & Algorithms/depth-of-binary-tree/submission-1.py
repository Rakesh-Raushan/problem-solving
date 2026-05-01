# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         self.max_depth = 0
#         depth = 0
#         self.helper(root, depth)
#         return self.max_depth

#     def helper(self,root, depth):
#         if not root:
#             return
#         depth+=1
#         self.max_depth = max(self.max_depth, depth)
#         self.helper(root.left, depth)
#         self.helper(root.right, depth)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #dfs solution
        from collections import deque
        queue = deque()

        if not root:
            return 0
        queue.append(root)
        depth = 0
        while(queue):
            # level trversal
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1
        return depth
        