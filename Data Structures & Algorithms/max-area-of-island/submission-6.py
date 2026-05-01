from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #bfs approach
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (0,1),(-1,0),(0,-1)]
        max_size = 0
        def bfs(i,j):
            queue = deque([(i,j)])
            grid[i][j] = "#"
            size = 1

            while queue:
                qi, qj = queue.popleft()
                for dx, dy in dirs:
                    nqi, nqj = qi+dx, qj+dy
                    if not ((0<=nqi<rows) and (0<=nqj<cols)) or grid[nqi][nqj] !=1:
                        continue
                    grid[nqi][nqj] = -1
                    size+=1
                    queue.append((nqi,nqj))
            return size
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size_i_j = bfs(i,j)
                    max_size = max(max_size, size_i_j)
        
        return max_size
                

        
        