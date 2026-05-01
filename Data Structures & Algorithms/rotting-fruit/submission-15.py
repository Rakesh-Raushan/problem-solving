class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        #if no fresh fruits then zero mins needed
        kind_of_cell_vals = set()
        for i in range(rows):
            for j in range(cols):
                kind_of_cell_vals.add(grid[i][j])
        if 1 not in kind_of_cell_vals:
            return 0
        #state not possible cases, return -1
        #if no rotten fruits then we will never have all rotten
        if 2 not in kind_of_cell_vals and 1 in kind_of_cell_vals:
            return -1
        #if any fruit can't be reached as neighbour of rotten fruit then
        # again we will never have all rotten case
        #for this we need to move neighbour to neighbour via bfs from every cell with rotten fruit
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        from collections import deque
        queue = deque()
        visited = set()

        #rotting will start simultaneously from all rotten fruits
        #so initially we add all to queue for bfs
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                    visited.add((i,j))

        time_taken = -1
        while queue:
            for _ in range(len(queue)):
                qi, qj = queue.popleft()
                for dx, dy in dirs:
                    ni, nj = qi+dx, qj+dy
                    if (0<=ni<rows) and (0<=nj<cols) and (not (ni,nj) in visited) and grid[ni][nj] != 0:
                        visited.add((ni,nj))
                        grid[ni][nj] = 2 #mark it rotten
                        queue.append((ni,nj))
            #update time after each level
            time_taken+=1        
        
        fresh_fruits_remaining = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==1:
                    fresh_fruits_remaining = True
        return time_taken if not fresh_fruits_remaining else -1
        
                    
                

            
        