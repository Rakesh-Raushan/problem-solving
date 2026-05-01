# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #idea is to create a string using preorder traversal but whenever we hit null node, we add a identifier for that
        res = []

        def dfs(root):
            #base case if null
            if not root:
                #we need to put an identifier string
                res.append("N")
                return
            #otherwise, do preorder i.e act on root, recurse left, recurse right
            #append the node val string
            res.append(str(root.val))
            #act on left
            dfs(root.left)
            dfs(root.right)

            #nothing to return as we are adding to res
        
        #call the func
        dfs(root)

        #return the single joined string
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #break the string to string list
        vals = data.split(",")
        #to traverse the string we will take a index
        self.idx = 0

        #helper dfs
        def dfs():   
            #base case if we find the null identifier
            if vals[self.idx] == "N":
                #move to next index and return a null
                self.idx+=1
                return None
            
            #else act on it to create a node
            node = TreeNode(int(vals[self.idx]))
            #increment index
            self.idx+=1

            #recurse on childrenok
            node.left = dfs()
            node.right = dfs()

            #return this node
            return node

        #call the func and return it
        return dfs()
