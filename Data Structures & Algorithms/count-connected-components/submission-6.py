class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #i can use a union find datastructure so and then use edges to union them repeatedly
        #every successful union would mean one less connected component so this way i can count the
        #number of successful unions to count the num of connected components

        #uf datastructure

        class UnionFind:
            def __init__(self, n):
                self.parent = {i:i for i in range(n)}
                self.rank = {i:0 for i in range(n)}
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                    #path compression
                return self.parent[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    #already connected components so cant union
                    return False
                if self.rank[px] < self.rank[py]:
                    self.parent[px] = py
                elif self.rank[py] < self.rank[px]:
                    self.parent[py] = px
                else:
                    self.parent[py] = px
                    self.rank[px]+=1
                return True
        
        uf = UnionFind(n)
        num_conn_comp = n
        for u,v in edges:
            if uf.union(u,v):
                num_conn_comp-=1
        return num_conn_comp
        