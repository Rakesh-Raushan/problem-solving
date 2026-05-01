class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #another approach (more popular) is to do inverse thinking
        #do dfs from boundary cells with 'O' and mark reachable 'O' from them as something else like "T"
        #then for the remaining cell with 'O' mark them as "X" as they will be surrounded ones
        #after that revert back the T cells the unsurrounded ones back to 'O'

        #let's write dfs that starts from 'O' cell and marks every 'O' cell reachable from there to 'T'
        # visited = set()
        def dfs(r,c):
            #BASE CASE: where we do not want to mark
            if min(r,c)<0 or r>=rows or c>=cols or board[r][c] != 'O':
                return
            #otherwise mark it with 'T'
            board[r][c]='T'
            # visited.add((r,c))

            #recurse on adjacent cells
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        #mark unsurrounded as "T"
        rows, cols = len(board), len(board[0])

        #iterate on boundary for 'O' cells and dfs to mark "T"
        for r in range(rows):
            for c in [0, cols-1]:
                if board[r][c] == 'O':
                    dfs(r,c)
        for c in range(1,cols-1):
            for r in [0, rows-1]:
                if board[r][c] == 'O':
                    dfs(r,c)

        #dfs will mark the unsurrounded as "T", so the left 'O' are surrounded
        #which we want to mark as "X"
        for  r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        #revert back the unsurrounded cells marked as "T" to 'O'
        for  r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
        #verification: [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","O"]]
        #all rows 0 col none
        #all rows 3 col got one match at (r=3,c=3), dfs(3,3)
        # marked (3,3) as 'T'
            #dfs(4,3) out of bounds > return
            #dfs(2,3) board[r][c] != 'O' > return
            #dfs(3,4) out of bounds > return
            #dfs(3,2) board[r][c] != 'O' > return
        #returned
        #board state: [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","T"]]
        #cols 1 and 0 row, no match, col 2 and 0 row no match
        #cols 1 and 3 row, no match, col 2 and 3 row no match

        #next iter for all rows and all cols looked for 'O' in board state: [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","T"]]
        #got match (1,1) > marked 'X', match (1,2) > marked 'X', match (2,1) > marked 'X', match (2,2) > marked 'X',
        #board state: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","T"]]

        #next iter for all rows and all cols looked for 'T'
        #match(3,3), marked 'O'
        #board state: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","O"]]
        #over

        