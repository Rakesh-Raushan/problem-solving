class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #essentially i need to find the number of connected components,
        #can i use union find #union till no new union possible #return num of components left
        #first approach DFS
        rows, cols = len(grid), len(grid[0])
        islands=0
        visited = set()
        def dfs(r, c):
            #neg base case
            if min(r,c)<0 or r>=rows or c>=cols or (r,c) in visited or grid[r][c]!="1":
                return
            
            #else recurse on adjacent
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="0" or (r,c) in visited:
                    continue
                dfs(r,c)
                islands+=1

        return islands
        

        