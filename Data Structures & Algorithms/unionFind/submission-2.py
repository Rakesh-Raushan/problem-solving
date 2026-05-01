class UnionFind:
    
    def __init__(self, n: int):
        #we simply maintain parent and rank of each node in hash map
        self.parent = {}
        self.rank = {}
        #we initialise the parent to node itself and rank to 0 for each node at start
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
        

    def find(self, x: int) -> int:
        #to find, we go to the parent of the node
        # p = self.parent[x]
        # #until we reach the condition p is parent of itself (as we initialised all nodes as parent of themselves)
        # while(p!=self.parent[p]):
        #     #we do what is called path compression, this help make the find efficient for repeated finds of the same node
        #     #this is an optional step to make find efficient
        #     self.parent[p] = self.parent[self.parent[p]]
        #     #keep moving up by updating p to its parent every time
        #     p = self.parent[p]
        # return p #when we are the top node 
        #this above find is not a full path compression but rather path halving and would require multiple find calls
        # to achieve full path compression
        #a better way to recurse and achieve full path compression in one go
        if self.parent[x]!=x:
            #move up as well as compress using recursion
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
        #this is better solution

    def isSameComponent(self, x: int, y: int) -> bool:
        px,py = self.find(x), self.find(y)
        if px==py:
            return True
        else:
            return False

    def union(self, x: int, y: int) -> bool:
        #get the parent using the find operation
        px, py = self.find(x), self.find(y)
        #if both already have same parent, we can not union them and we return false
        if px == py:
            return False
        #if not so we can just combine the parents arbitrarily but we would rather combine based on rank
        
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            #if both have same rank, make anyone the parent of other and increase the rank of parent
            self.parent[px] = py
            self.rank[py]+=1
        return True #marks successful union       

    def getNumComponents(self) -> int:
        disjoint_comp = set([self.find(x) for x in self.parent])
        return len(disjoint_comp)

