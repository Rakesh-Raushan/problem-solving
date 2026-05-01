class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = {}

        for i in range(1,n+1):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x):
        if not self.parent[x]==x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px,py = self.find(x), self.find(y)
        
        if px==py:
            return False
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py]+=1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        my_union_find = UnionFind(n)
        
        result = []
        for i in range(n):
            if not my_union_find.union(edges[i][0], edges[i][1]):
                result.append(edges[i])
            i+=1
        return result[-1]
        


        