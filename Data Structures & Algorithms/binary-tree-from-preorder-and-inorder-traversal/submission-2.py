# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #we can build a solution based on the idea that preorder give the order of roots
        #and for a root, its poition partitions the inorder to gives us left nodes and right nodes
        #we will take take two pointers to identify the left and right of partitions and work with
        #sucessive root via recursion

        def helper(preorder_idx, left_inorder, right_inorder):
            if preorder_idx >= len(preorder) or left_inorder > right_inorder:
                return None
            
            node_val = preorder[preorder_idx]
            node = TreeNode(val = node_val)
            node_inorder_idx = inorder.index(node_val)
            num_left_nodes = node_inorder_idx - left_inorder
            
            #here cruicial thing to take care of is that for this 
            #to build its left and right children, call helper with updated args
            node.left = helper(preorder_idx+1, left_inorder, node_inorder_idx-1)
            node.right = helper(preorder_idx+1+(num_left_nodes), node_inorder_idx+1, right_inorder)

            #after building its children, return this node
            return node
        
        return helper(0,0,len(preorder)-1)

        # # Create a map for quick index lookup in inorder
        # idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        # def helper(pre_start, in_start, in_end):
        #     if pre_start >= len(preorder) or in_start > in_end:
        #         return None
            
        #     root_val = preorder[pre_start]
        #     root = TreeNode(root_val)
        #     in_idx = idx_map[root_val]
        #     left_size = in_idx - in_start
            
        #     root.left = helper(pre_start + 1, in_start, in_idx - 1)
        #     root.right = helper(pre_start + 1 + left_size, in_idx + 1, in_end)
            
        #     return root
        
        # return helper(0, 0, len(inorder) - 1)

        #verify Input: preorder = [1,2,3,4], inorder = [2,1,3,4] # Output: [1,2,3,null,null,null,4]
        # preorder_idx = 0, left_inorder = 0, right_inorder = -1, len(preorder)=4
        # 0<4, node_val = 1, node = N(1), node_inorder_idx = 1
                            # node.left
                                # (1,0,1)
                                # 1<4, node_val = 2, node - N(2), node_inorder_idx = 0
                                        #node.left
                                        #(2,0,0)
                                        #2<4, node_val = N(3), node_inorder_idx = 2
                                            #node.left
                                            #(3,0,)

        