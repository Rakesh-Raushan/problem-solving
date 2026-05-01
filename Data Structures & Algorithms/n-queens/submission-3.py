class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #recursive solution

        results = []
        cols = set()
        pos_diag = set()
        neg_diag = set()

        board = [["."]*n for _ in range(n)]
        queens=0

        def helper(r):
            #BASE POS CASE
            if r==n:
                results.append(["".join(row) for row in board])
                return

            #if not so for this row check for all the columns
            for c in range(n):
                if c in cols or r+c in pos_diag or r-c in neg_diag:
                    continue
                #you found a col which is okay to place queen for this row
                board[r][c] = "Q"
                #update the cols, pos_diag and neg_diag
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)

                #recurse on next row
                helper(r+1)

                #backtrack
                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
        
        helper(0)

        return results

#verify n=4, helper(r=0), cols = {}, pos_diag = {}, neg_diag = {}
# r=0 c=0, [0][0]-Q, cols = {0}, pos_diag = {0}, neg_diag = {0}
        #recurse helper(r=1)
        # r=1, c=0, c in cols so skip
        # r=1, c=1, r-c in neg_diag so skip
        # r=1, c=2, [1][2]=Q, cols = {0,2}, pos_diag = {0,3}, neg_diag = {0,-1}
            #recurse on helper(r=2)
            #r=2,c=0, c in cols so skip
            #r=2, c=1, r+c in pos_diag so skip
            #r=2, c=2, r-c in neg_diag
            #r=2, c=3, r-c in neg_diag so skip 
            # range over return
            #pop additions
        #pop additions
# r=0, c=1 [0][1]=Q, cols = [1], pos_diag = [1], neg_diag = [-1]
        #recurse helper(r=1)
        #r=1, c=0, r+c in pos diag so skip
        #r=1, c=1, c in cols so skip
        #r=1, c=2 , r-c in neg diag so skip
        #r=1,c=3, [1][3] =Q cols = [1,3], pos_diag = [1,4], neg_diag = [-1,-2]
            #recurse helper(r=2)
            #r=2, c=0, =Q cols = [1,3,0], pos_diag = [1,4,2], neg_diag = [-1,-2,2]
                #recurse helper(r=3)
                #r=3,c=0 c in col skip
                #r=3, c=1, r-c in neg diag skip
                #r=3, c=2, [3][2]=Q
                #recurse helper(r=4)
                #BASE case so add to result = [[.,Q,.,.], [.,.,.,Q],[Q,.,.,.],[.,.,Q,.]]
                #

        