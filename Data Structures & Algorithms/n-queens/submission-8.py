class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #idea is to start from 0th column and explore 
        #all possible paths for different positions of queen
        possible_sols = []

        board = [['.']*n for _ in range(n)]

        cols = set()
        pos_diag = set()
        neg_diag = set()

        #recursive helper that can act on a row to continue placing queens

        def helper(r):
            #if we have reached the last row, it means our current board is valid solution
            if r==n:
                possible_sols.append(["".join(row) for row in board])
                #no need to recurse any further
                return

            #otherwise we need to find a position/ col in this row to place queen
            #iterate on all cols, 
            #To track if a cell belongs to a col, we can simply check if the col num was seen ealier via col_set
            #but to check if a cell belongs to a pos diag, we can do so by tracking r+c in pos dia num
            #for any cell in that diag r+c will be const and 
            # and for who
            for c in range(n):
                if c in cols or r+c in pos_diag or r-c in neg_diag:
                    continue
                #else, this is a valid col for queen to place for this row so mark it used
                board[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                #and recurse on next row
                helper(r+1)
                #for other poss combination, backtrack after resetting the board
                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
            
        helper(0)

        return possible_sols


        

        