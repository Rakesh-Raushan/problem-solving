# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     #Empty
    #     if not root:
    #         return root

    #     #path to nodes
    #     path_p = self.get_path(root, p, [])
    #     path_q = self.get_path(root, q, [])

    #     #look for common one in the path
    #     i=0
    #     while i < min(len(path_p), len(path_q)) and path_p[i].val == path_q[i].val:
    #         i+=1
    #     return path_p[i-1]

    # #dfs recursive
    # def get_path(self, root, node, path):
    #     #empty
    #     if not root:
    #         return path
    #     path.append(root) #inplace
    #     if root.val == node.val:
    #         #node found
    #         return path
    #     if root.left:
    #         self.get_path(root.left, node, path)
    #         #see if node was found in the path, then return
    #         if path[-1].val == node.val:
    #             return path
    #         else:
    #             #bring back path state for backtrack and going to right
    #             path.pop()
    #     if root.right:
    #         self.get_path(root.right, node, path)
    #         if path[-1].val == node.val:
    #             return path
    #         else:
    #             path.pop()

    # #this solution works but you missed a big fact that this was a BST and your solution is for a general case
    # #for BST it is such a small solution using the fact that, the node at which one is greater than value and other lower than is the LCA

        #make sure p is smaller value
        if p.val > q.val:
            p, q = q, p
        
        #do both left and right lie in opp subtrees of curr then this is the LCA
        if p.val <= root.val <= q.val: #note = check despite BST, bcoj, two nodes being compared might be the same node root and no left, root becomes LCA of root and and right
            return root
        elif p.val < root.val and q.val < root.val:
            #both lie in left so LCA must be down left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            #both lie in right so LCA must be down right subtree
            return self.lowestCommonAncestor(root.right, p, q)
           



            
        