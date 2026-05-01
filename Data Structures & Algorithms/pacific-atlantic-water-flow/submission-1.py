class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #BIG IDEAS:
        #DFS on Pacific cells upper and left border cells to mark cell reachable from them as pacific cells
        #DFS on Atlantic cells lower and right border cells to mark cells reachable from them as atlantic cell
        #Cell marked as both pacific and atlantic will be our solution provided
            #In DFS we consider flow only to higher than or equal to cells in height
            #because question asks cells from which water can flow to both oceans

        rows, cols = len(heights), len(heights[0])
        #to mark reachability
        pacific = set()
        atlantic = set()

        #helper dfs pacific
        def dfs(r,c, visited):
            #if pacific, we can go to lower heigh cells
            #BASE case
            if (r,c) in visited:
                return            

            visited.add((r,c))
            #explore its adjacent cells
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                #if lower height
                if 0<=r+dr<rows and 0<=c+dc<cols and (r+dr,c+dc) not in visited and heights[r+dr][c+dc] >= heights[r][c]:
                    dfs(r+dr, c+dc, visited)

        
        pacific_cells = [(r,0) for r in range(rows)] + [(0,c) for c in range(cols)]
        atlantic_cells = [(r,cols-1) for r in range(rows)] + [(rows-1,c) for c in range(cols)]
        #iterate on pacific
        for cell in pacific_cells:
            if cell not in pacific:
                dfs(cell[0], cell[1], pacific)
        #iterate on atlantic
        for cell in atlantic_cells:
            if cell not in atlantic:
                dfs(cell[0], cell[1], atlantic)

        #cells in both atlantic and pacific should be our results
        result = [list(common_cell) for common_cell in pacific.intersection(atlantic)]

        return result

#verify:
#         [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]
#dfs_p(4), pacific = {4} 
    #dfs_p(2) pacific = {4,2} return
#dfs_p(7), pacific = {4,2,7}, 
    #dfs(6) pacific{4,2,7,6},
        #dfs(3) pacific{4,2,7,6,3} return 
#7



        

        
