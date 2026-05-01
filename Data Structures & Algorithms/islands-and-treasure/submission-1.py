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
            
            for r in range(rows):
                for c in range(cols):
                    #run bfs simultaneously from all treasures so add all of them to queue
                    if grid[r][c] == 0:
                        queue.append((r,c))

            while queue:
                r, c = queue.popleft()

                directions = [(1,0), (-1,0),(0,1),(0,-1)]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <=nc < cols and grid[nr][nc]==2147483647:
                        grid[nr][nc] = grid[r][c] + 1 #starting from treasure cell of 0 so +1 works from start
                        queue.append((nr,nc))

                    
