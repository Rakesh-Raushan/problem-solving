class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #9:09
        # TWO BIG IDEAS OF THE SOLUTION:
            # YOU NEED BFS to do min dist calculations and you need to run them from treasures and not INF cells
            # ALSO, the BFS MUST run simultaneously from all the treasure cells (Start of queue is all treasure cells in it)
            # else you will mark all distances with the dist from first treasure cell you run the BFS on

            from collections import deque
            rows, cols = len(grid), len(grid[0])
            queue = deque()
            visited = set()
            
            for r in range(rows):
                for c in range(cols):
                    #run bfs simultaneously from all treasures so add all of them to queue
                    if grid[r][c] == 0:
                        queue.append((r,c))
            
            #start position set
            dist=0

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    #for any cell reachble from here mark it 1 if curr is INF else curr +1
                    if grid[r][c]==2147483647:
                        grid[r][c] = dist
                        visited.add((r,c))
                    #add neighbours
                    directions = [(1,0), (-1,0),(0,1),(0,-1)]
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if min(nr, nc)>=0 and nr<rows and nc<cols and (nr, nc) not in visited and grid[nr][nc]==2147483647:
                            queue.append((nr,nc))
                dist+=1

                    
