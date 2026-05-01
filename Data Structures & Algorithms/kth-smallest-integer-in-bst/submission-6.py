# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            #go as left as poss
            while curr:
                stack.append(curr)
                curr = curr.left
            #if no more curr, go back to last root using stack and that count this for your kth thing
            curr = stack.pop()
            k-=1
            if k==0:
                return curr.val
            #else go to right node
            curr = curr.right
        
        