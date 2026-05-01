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

#above can be one liner also:
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

#or it can be iterative dfs also, stack based
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        stack = []
        #initialize the stack with root node and depth 1 as a single node has 1 node on path, i.e depth =1
        stack.append((root,1))

        while(stack):
            #get the node and depth
            node, depth = stack.pop()
            #check if this depth is higher than we have seen so far and if so update our res
            res=max(depth, res)

            #add its children to stack with 1 higher depth
            if node.left:
                stack.append((node.left,depth+1))
            if node.right:
                stack.append((node.right,depth+1))
        
        #having covered the whole tree this way, we are sure the res is what max depth we have seen at any node
        return res




#we can have BFS level wise traversal solution also:
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         #dfs solution
#         from collections import deque
#         queue = deque()

#         if not root:
#             return 0
#         queue.append(root)
#         depth = 0
#         while(queue):
#             # level trversal
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             depth+=1
#         return depth
        