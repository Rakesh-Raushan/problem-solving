# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # self.inorder_list = []
        # self.k = k
        # def inorder_traversal(root):
        #     if not root:
        #         return
            
        #     #recurse on left
        #     inorder_traversal(root.left)
        #     self.inorder_list.append(root.val)
        #     inorder_traversal(root.right)
        
        # inorder_traversal(root)
        
        # return  self.inorder_list[k-1]

        #the above method does the entire traversal even if k =1; we can do early termination and for that we would need
        #iterative inorder traversal

        #iterative inorder

        def iterative_inorder(root):
            
            #stack
            stack = []
            # res = []
            i=0

            while root or stack:
                if root:
                    #add this on stack and move to process left first
                    stack.append(root)
                    root = root.left
                else:
                    root = stack.pop()
                    #act on root
                    # res.append(root.val)
                    i+=1
                    if i==k:
                        return root.val
                    
                    # if len(res)==k:
                    #     break
                    #move right
                    root = root.right
            # return res[-1]
        
        return iterative_inorder(root)
                        


        