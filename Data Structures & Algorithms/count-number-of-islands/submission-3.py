class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(i,j):
            if not ((0<=i<rows) and (0<=j<cols)) or grid[i][j]!="1":
                return False
            grid[i][j] = "#"
            for dx, dy in dirs:
                ni, nj = i+dx, j+dy
                dfs(ni,nj)
            return True

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    if dfs(i,j):
                        count+=1
        return count

        