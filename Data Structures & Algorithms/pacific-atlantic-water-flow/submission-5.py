class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #for every cell check if we can dfs to pacific cells or atlantic cells
        #pacific cells = row=0 or col=0
        #atlantic cells = row=m-1, col = n-1
        rows, cols = len(heights), len(heights[0])
        pacific_set = set([(0,i) for i in range(cols)] + [(i,0) for i in range(rows)])
        atlantic_set = set([(rows-1,i) for i in range(cols)] + [(i,cols-1) for i in range(rows)])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    
        def dfs_pacific(r,c):
            #if invalid cells to move to, return
            if (r,c) in visited:
                return
            visited.add((r,c))       
            for dr, dc in dirs:
                nr, nc = r+dr, c + dc
                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc] >= heights[r][c]:
                    #water can flow towards pacific
                    pacific_set.add((nr,nc))
                    dfs_pacific(nr,nc)

        def dfs_atlantic(r,c):
            #if invalid cells to move to, return
            if (r,c) in visited:
                return
            visited.add((r,c))
            for dr, dc in dirs:
                nr, nc = r+dr, c + dc
                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc] >= heights[r][c]:
                    #water can flow towards pacific
                    atlantic_set.add((nr,nc))
                    dfs_atlantic(nr,nc)

        #slightly diff approach we should take
        #we should first gather cells reachable from top and left cells as pacific connected
        pacific_cells = list(pacific_set)
        atlantic_cells = list(atlantic_set)
        for r,c in pacific_cells:
            visited = set()
            dfs_pacific(r,c)
        for r,c in atlantic_cells:
            visited = set()
            dfs_atlantic(r,c)
        
        both_pacific_atlantic = [list(x) for x in pacific_set if x in atlantic_set]

        return both_pacific_atlantic

        