class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #i can find just the max area or can also find the area of all islands and pick max
        # for that i think the approach will be to dfs from each land cell and cover as much as possible
        # marking visited in place and also measuring the area as we dfs recusively
        #update areas list after each dfs

        rows, cols = len(grid), len(grid[0])
        island_areas = [0]
        visited = set()

        dirs = [(1,0),(0,1), (-1,0),(0,-1)]
        def dfs(r,c):
            nonlocal area
            if not 0<=r<rows or not 0<=c<cols or (r,c) in visited or grid[r][c]==0:
                return
            visited.add((r,c))
            area+=1
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                dfs(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    #land cell, calculate area
                    area=0
                    dfs(r,c)
                    island_areas.append(area)
        
        return max(island_areas)
        