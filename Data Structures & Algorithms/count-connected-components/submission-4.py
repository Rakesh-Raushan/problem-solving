#we will define a unionfind class
#sometimes we also name the class as DSU signifying disjoint set union
#idea is to have a data structure for n nodes which maintains the root information and height information
#for all the disconnected components in a graph of these n nodes (1 or more) and allow finding the root (super parent)
#as well as allow merging or union of two disconnected components via find and union methods respectively

class unionFind:
    def __init__(self, n):
        #we use a hash map to store the parent info, initially we assume all n nodes to be disconnected as we only have
        #information of the number of nodes
        self.parent = {i:i for i in range(n)}
        #we also maintain a hash map to store the info of height/rank of each disconnected component
        #initially as we assume that each node is disconnected, rank is 0 for each
        self.rank = {i:0 for i in range(n)}

    #a method to find the super parent / root of components in the graph given a node in the component
    def find(self, x):
        #idea to keep looking at parents to parents unless for a node,node itself is parent, the starting condition
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
        #further we do path shorting to make subsequent find operation efficient by updating the parent of nodes
        #exlored
        return self.parent[x]

    #a method to union two disconnected components in the graph
    def union(self, x, y):
        #get the parents of both the nodes first using our find operation defined
        px, py = self.find(x), self.find(y)

        #if both have the same parent they are already part of same component and no union can be done
        if px == py:
            #same parent return false as output of union
            return False
        
        #if not so, we should merge the smaller component to the bigger for more efficient finds in future
        #called rank based merging
        if self.rank[px] > self.rank[py]:
            #merge py to px, by updating the parent of py as px
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            #merge px to py, by updating the parent of px as py
            self.parent[px] = py
        else:
            #for same rank merge any to any but update rank for the one we merge to
            self.parent[px] = py
            self.rank[py]+=1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #we can use the defined unionFind class to count the components
        uf = unionFind(n)

        #since we have the edge information, we can use the union to create the connected components
        #out of the initial all n disconnected components created in the unionFind uf
        for edge in edges:
            x,y = edge
            uf.union(x,y)
        
        #after running the union based on edges, we can look at unique parents to get num of components
        parents = {uf.find(x) for x in range(n)}

        return len(parents)

        

        
        