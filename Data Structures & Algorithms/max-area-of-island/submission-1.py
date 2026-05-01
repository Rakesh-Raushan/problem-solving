class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #we can solve it using recursion and backtracking
        #dfs
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def helper(r,c, curr_area):
            #base case, out of boundary, zero case, visited case
            if min(r,c)<0 or r>=rows or c>=cols or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))

            curr_area[0]+=1

            helper(r+1,c, curr_area)
            helper(r-1,c, curr_area)
            helper(r,c+1, curr_area)
            helper(r,c-1, curr_area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and not (r,c) in visited:
                    curr_area = [0]
                    helper(r,c, curr_area)
                    max_area = max(max_area, curr_area[0])
        return max_area