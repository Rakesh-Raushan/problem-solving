# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        #this should be easy and simply we can do BFS with queue and a level order loop

        from collections import deque
        queue = deque()
        queue.append(root)
        results = []
        while(queue):
            curr_level_nodes = []
            for i in range(len(queue)):
                node = queue.popleft()
                curr_level_nodes.append(node.val)
                #push its children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            results.append(curr_level_nodes)
        
        return results


        