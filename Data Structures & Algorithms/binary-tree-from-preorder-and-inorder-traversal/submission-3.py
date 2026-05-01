# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #we can build a solution based on the structure that:
            # preorder -> root, [its left nodes], [its right nodes]
            # inorder -> [its left nodes], root, [its right nodes]
        #use preorder index to pick root of subtree
        #build the root node of subtree
        #find index of this root node in inorder array
        #use this inorder index to calculate the num of left children,
            #use no. of left children to decide the preorder starting index for left and right children
                #for left = preorder_idx + 1
                #for right = preorder_idx + count_left_children + 1
        #use inorder index of root to decide inorder range for left and right
            #for left = (root_left, inorder_indx -1)
            #for right = (inorder_indx + 1, root_right)

        #repeat above under base condition to return None if
            # preorder start idx >= len(preorder)
            # inorder start > inorder end
        #based on preorder index we can get node value and build a root node
        #to build its children left and right, we can use same function

        inorder_map = {x:idx for idx,x in enumerate(inorder)}

        def helper(pre_start, in_start, in_end):
            if pre_start >= len(preorder) or in_start > in_end:
                return None
            
            #use pre_start to build subtree root
            node_val = preorder[pre_start]
            node = TreeNode(val = node_val)

            #to build its children we use inorder index of this, we can build a hashmap and use it
            inorder_idx_node = inorder_map[node_val]
            #no of left children
            count_left = inorder_idx_node - in_start

            #recurse to get left with new pre_start, old in_start, new in_end
            node.left = helper(pre_start+1, in_start, inorder_idx_node - 1)
            #recurse to get right with new pre_start, new in_start, old in_end
            node.right = helper(pre_start + count_left + 1, inorder_idx_node + 1, in_end)

            return node
        #run the helper with starting conditions, preorder start of 0, inorder start 0, inorder end len(inorder)-1
        return helper(0, 0 , len(inorder)-1)

        