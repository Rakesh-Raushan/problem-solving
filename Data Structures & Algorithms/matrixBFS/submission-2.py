class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        from collections import deque

        n_rows, n_cols = len(grid), len(grid[0]) #3,3
        queue = deque() 
        visited = set()

        #add the starting point

        queue.append((0,0))
        visited.add((0,0))

        length = 0
        while(queue):
            #do it level by level so that we can increase the length only after a level is
            #covered
            for i in range(len(queue)):
                r, c = queue.popleft() #0,0 #0,1

                if r == n_rows-1 and c == n_cols-1:
                    # we have already reached the target cell at this level and length
                    return length
                
                neighbours = [1,0], [-1,0], [0,1], [0,-1]

                for nd, cd in neighbours: #(1,3), (-1,3), (0,4), (0,2)
                    new_r, new_c = r+nd, c+cd
                    #check if it is a valid path if now skip this 
                    if min(new_r, new_c) <0 or new_r == n_rows or new_c == n_cols or grid[new_r][new_c]==1 or (new_r, new_c) in visited:
                        continue
                    #if not then add the neighbours to queue
                    # left with only(0,1), this time (0,2) only, this time (1,2) and (0,3), #(2,2) and (1,3) #
                    queue.append((new_r, new_c))
                    #mark visited so that we do not process them again for the same level
                    visited.add((new_r, new_c))
            #update length for next level by 1 unit
            length+=1 # 1 now, # 2 now # 3 now
        
        return -1



        