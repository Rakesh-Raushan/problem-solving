class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #we will need trigger a simultaneous BFS from each treasure chest to mark the nearest
        #distance

        rows, cols = len(grid), len(grid[0])

        treasure_cells = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    treasure_cells.append((i,j))
        
        from collections import deque
        queue = deque(treasure_cells)
        visited = set(treasure_cells)

        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        dist = 1
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    #if it is a valid, unvisited and inf land cell
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc] ==2147483647:
                        #mark the distance and mark visited
                        grid[nr][nc]=dist
                        visited.add((nr,nc))
                        #add them to queue for bfs
                        queue.append((nr,nc))
            dist+=1
        

        