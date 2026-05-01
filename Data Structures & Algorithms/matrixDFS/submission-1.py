class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def dfs(grid, r, c, visited):
            n_rows, n_cols = len(grid), len(grid[0])
            #base cond
            #1
            if min(r,c)<0 or r==n_rows or c==n_cols or (r,c) in visited or grid[r][c]==1:
                #either outside left upper or outside lower right or already visited or
                #its a rock
                return 0
            #2
            if r==n_rows-1 and c==n_cols-1:
                #target cell and so a valid path
                return 1

            #mark it visited
            visited.add((r,c))

            #initialize count to 0
            count = 0

            #recurse on other possible paths
            count+= dfs(grid, r+1,c,visited)
            count+= dfs(grid, r-1,c,visited)
            count+= dfs(grid, r,c+1,visited)
            count+= dfs(grid, r,c-1,visited)

            #remove from visited when backtracking to enable alternate path visits
            visited.remove((r,c))

            return count

        visited = set()
        count_paths = dfs(grid,0,0,visited)
        return count_paths
        