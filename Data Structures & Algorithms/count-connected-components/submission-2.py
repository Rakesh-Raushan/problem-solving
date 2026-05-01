#sometimes you will see DSU as the class name instead of unionFind, DSU stands for disjoint set union
class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px,py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.rank[px] > self.rank[py]:
            print("updating: parent x has higher rank", x,y)
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            print("updating: parent y has higher rank", x,y)
            self.parent[px] = py
        else:
            print("updating: parent x has same rank", x,y)
            self.parent[px] = py
            self.rank[py]+=1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)
        for edge in edges:
            x,y = edge[0], edge[1]
            uf.union(x,y)
            print(uf.parent)

        unique_parents = set()
        for i in range(n):
            parent_i = uf.find(i)
            unique_parents.add(parent_i)

        
        return len(unique_parents)

        