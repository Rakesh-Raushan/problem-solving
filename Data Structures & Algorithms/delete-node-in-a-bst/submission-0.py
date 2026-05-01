# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #if it the root itself or say root is null
        if not root:
            return root
        
        if key > root.val:
            #we need to do delete op in right subtree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            #we need to do delete op in left subtree
            root.left = self.deleteNode(root.left, key)
        else:
            #we have arrived at the node to be deleted
            #check if it is 0/1 case, can be solved easily
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                #means it has 2 children, so need to replace with min of rt subtree or max of left subtree
                curr = root.right #right subtree
                while curr.left:
                    curr = curr.left
                #got the min, replace root val with it
                root.val = curr.val
                #now delete the min val node in the right sub
                root.right = self.deleteNode(root.right, root.val)
        return root
            




        