class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #input grid and a word
        #output exp: true if word in grid else false
        #same path can not be used again in a word, movements only horizontal and vertical
        #unless there is a match, i'll not increase the index
        #if match, i'll increase index and recurse on 4 possible paths from there

        #from a cell, not allowed paths
        # boundary conditions both , path cells

        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            #base condition pos case: we reached end of word mark
            if i==len(word):
                return True
            #base condition neg, 
            #check (out of bound + if the char in grid does not match the word + if char in grid has been visited
            if (r<0 or c <0 or 
                r==rows or c==cols or
                board[r][c] != word[i] or 
                (r,c) in path):
                return False
            
            # if board[r][c] == word[i]: no need to check as not condition already checked before it
            #mark it on path
            path.add((r,c))
            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or  dfs(r,c+1,i+1) or dfs(r,c-1,i+1)

            if not res:
                path.remove((r,c))
            return res
            

        for r in range(len(board)): #012
            for c in range(len(board[0])):#0123
                if dfs(r, c, 0) == True: #00 01 02c
                    return True
        
        return False


        