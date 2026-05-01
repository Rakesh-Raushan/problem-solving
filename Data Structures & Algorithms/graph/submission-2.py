class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        self.graph[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if dst in self.graph:
            if src in self.graph:
                if dst in self.graph[src]:
                    self.graph[src].remove(dst)
                    return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        #path between two nodes
        # to assume src and dst are in graph
        # dfs
        # from collections import deque

        # stack = deque()
        # visited = set()
        # stack.append(src)
        # visited.add(src)

        # while(stack):
        #     node = stack[-1]
        #     if dst == node:
        #         return True
        #     neighbours = self.graph[node]
        #     uv_node = [x for x in neighbours if x not in visited]
        #     if uv_node:
        #         next_node = uv_node[0]
        #         stack.append(next_node)
        #         visited.add(next_node)
        #     else:
        #         stack.pop()
        # return False
        #try recursive dfs
        def dfs(src, dst, visited):

            #base case:
            if src == dst:
                return True
            
            visited.add(src)
            found = False
            neighbours = self.graph[src]

            for neighbour in neighbours:
                print(f"checking: {neighbour}, visited state: {visited}")
                if neighbour in visited:
                    continue
                found= dfs(neighbour, dst, visited)
                if found:
                    break
            
            visited.remove(src)
            return found
        
        return dfs(src,dst,set())



