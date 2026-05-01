class unionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(1, n+1)}
        self.rank = {i:0 for i in range(1, n+1)}

    def find(self, x):
        if self.parent[x] != x:
            #it is not super parent, do path compression
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            #same parents >> connected components >> union not possible
            return False
        elif self.rank[px] > self.rank[py]:
            #y should merge to x, as x parent is the one with higher rank
            self.parent[y] = px
        elif self.rank[py] > self.rank[px]:
            #x should merge to y, as y parent is the one with higher rank
            self.parent[x] = py
        else:
            #both parents have same rank so any can merge to any
            self.parent[px] = py
            self.rank[px]+=1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #i am thinking if i run union find on n nodes, with every union i would connect two
        #if i traverse edges from left to right and keep checking for connected components
        n = len(edges)
        uf = unionFind(n)
        redundant_connections = []
        for edge in edges:
            print(uf.parent)
            print(uf.rank)
            if not uf.union(edge[0], edge[1]):
                redundant_connections.append(edge)
        
        return redundant_connections[-1]


        