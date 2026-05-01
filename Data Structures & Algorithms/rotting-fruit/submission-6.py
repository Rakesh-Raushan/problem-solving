class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        from collections import deque
        queue = deque()
        visited = set()
        no_fresh_fruits = True
        for r in range(rows):
            for c in range(cols):
                #check for fresh fruits simultaneously
                if grid[r][c] == 1:
                    no_fresh_fruits = False
                if grid[r][c] == 2:
                    #rotten fruit
                    queue.append((r,c))
                    #also make their val = 0
                    grid[r][c] = 0
        #no fresh fruits so min time = 0
        if no_fresh_fruits:
            return 0
        #no rotten fruits case, min time to rot not possible return -1
        if not queue:
            return -1
        
        
        while queue:
            r, c = queue.popleft()
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc] == 1:
                    queue.append((nr,nc))
                    #make their value as rotting time by adding 1 to parent cell val
                    grid[nr][nc] = 1 + grid[r][c]
                    visited.add((nr,nc))
        
        print(grid)
        #check if any unrotten fruit left
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    return -1


        time = max([max(l) for l in grid])

        return time 

        