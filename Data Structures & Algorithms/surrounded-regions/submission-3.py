class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #a region can be considered surrounded if we start from one 0 cell in the region and dfs to other os and do not end up to say boundary cells

        rows, cols = len(board), len(board[0])
        visited = set()

        def helper(r, c):
            if min(r,c)<0 or r>=rows or c>=cols:
                return False
            
            if board[r][c] == "X" or (r,c) in visited:
                return True
            
            visited.add((r,c))

            return helper(r+1,c) and helper(r-1,c) and helper(r, c+1) and helper(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    surrounded = helper(r,c)
                    if surrounded:
                        #mark all in visited as "X":
                        for cell in visited:
                            board[cell[0]][cell[1]] = "X"
                    visited = set()
                    

        