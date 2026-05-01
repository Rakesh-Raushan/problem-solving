# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #an easy solution is to do level order traversal and siimply maintain the max see before that level
        #no this is utterly wrong, by level approach you can't determine anything related to path

        # Only a DFS based approach can work, also if we need to do a preorder so that befor deciding on any children
        # we first have evaluated their root for max so far
        self.count = 0
        self.max_so_far = [float("-inf")]
        self.count_good_nodes(root)

        return self.count

    def count_good_nodes(self, root):

        if not root:
            return
        updated = False
        #process root first
        if root.val >= self.max_so_far[-1]:
            self.count+=1
            #update max so far also
            updated = True
            self.max_so_far.append(root.val)
        #process its children
        if root.left:
            self.count_good_nodes(root.left)
        if root.right:
            self.count_good_nodes(root.right)
        #return to last max for backtracking and next exploration
        if updated:
            self.max_so_far.pop()

    #verify root=[3,1,4,3,null,1,5]
    # count=0, msf= -inf, call(3) -> 3>-inf so count=1,msf=3, call on 3 children
        # call on 3_left call(1) -> 1< so nothing, call on 1 children
            # call on 1_left call(3) -> 3>=3 so count=2,msf=3,call on right child of 1
            # call on 1_right call(None) -> return to last
        #call on 3_right call(4) -> 4>3 so count = 3, msf = 4, call on 4 children
            #call on 4_left call(1), 1<4 return 
            #call on 4_right call(5), 5>4, so count = 4, msf=5, return to last
        #return to last
    #return to main
    #return count = 4 ans, so wrks
            
        

        