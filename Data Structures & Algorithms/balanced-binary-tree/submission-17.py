# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #brute force way would be to just go to everynode 
        #calculate the height of that node left and right sub and check isbalanced
        #this would lead to n(logn) for balanced tree and for a skewed tree can go even n^2
        #brute implementation
        #---------
        # def getHeight(root):
        #     #no node has 0 height
        #     if not root:
        #         return 0
        #     #otherwise height is max of height of its two subtrees + 1 extra node to its subtree
        #     return 1+ max(getHeight(root.left), getHeight(root.right))
        
        # if not root:
        #     return True
        # #no node tree is balanced so true
        # #else check this tree is balanced and also both its subtree are balanced
        # elif abs(getHeight(root.left) - getHeight(root.right)) > 1:
        #     return False
        # else:
        #     return self.isBalanced(root.left) and self.isBalanced(root.right)
        #---------------
        #however, it is clear that we can check the height and isbalanced together also
        #to optimize it to O(n) - linear
        #i can take help of a helper dfs to return both the info as i traverse
        #----------------
        # def dfs(root):
        #     if not root:
        #         return [True, 0] #i.e it is balanced 0 index and its height is 0, index 1
        #     #do it for the children
        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     #both children should be balanced and this node should be balanced
        #     isbalance = left[0] and right[0] and not abs(left[1] - right[1]) > 1
        #     return [isbalance, 1 + max(left[1], right[1])] #other wise propagate the height along with balanced
        
        # #use this to get the tree balance info
        # return dfs(root)[0]
        #-----------------
        #we can even further improvise it by using specific height value itself to signify imbalance
        def dfs(root):
            if not root:
                return 0 #i.e it is balanced 0 index and its height is 0, index 1
            #do it for the children
            left = dfs(root.left)
            right = dfs(root.right)

            #both children should be balanced and this node should be balanced
            #if imbalance, we return height -1 else the actual height
            if left ==-1 or right == -1 or abs(left - right)>1:
                return -1
            else:
                return 1 + max(left, right)

        #use this to get the tree balance info
        return dfs(root) != -1
        