class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs approach
        rows, cols = len(grid), len(grid[0])
        from collections import deque
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        def bfs(i,j):
            queue = deque([(i,j)])
            grid[i][j] = "#"

            while queue:
                qi, qj = queue.popleft()
                for dx, dy in dirs:
                    nqi, nqj = qi + dx, qj + dy
                    if not ((0<=nqi<rows) and (0<=nqj<cols)) or grid[nqi][nqj] !="1":
                        continue
                    grid[nqi][nqj] = "#"
                    queue.append((nqi,nqj))
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i,j)
                    count+=1
        return count


        