# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #diameter will the max length through a node
        #or we can say max(all path through all nodes)
        #one imp details to remm here is we already have something for max path from a node
        #which we call the height. to manage the max, we can pass a reference var like list
        #also, clearly for getting the max path for any node it will depend on its child max left
        #and right heights so, we should take post dfs approach
        
        def dfs(root, max_path):
            if not root:
                return 0
        
            left_h = dfs(root.left, max_path)
            right_h = dfs(root.right, max_path)

            #max path through the root = left_h + right_h
            max_path[0] = max(max_path[0], left_h + right_h)
            return 1 + max(left_h, right_h)
        
        max_path = [0]
        dfs(root,max_path)
        
        return max_path[0]


# root = [1,null,2,3,4,5]
# max_path = [],
# 1 -> left_h = (null), right_h = (2)
#               0 ,             
#                           left_h = (3), right_h = (4)
#                               (5) (null)          (null) (null)
#                                   (null)(null),0      0
                        #         max_path[0] = 0,
                        #     max_path[0] = 1, 
                        # max_path[0] = 2+1 = 3
